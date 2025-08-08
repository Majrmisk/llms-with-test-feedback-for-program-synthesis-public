import os
import re
import sys
import shutil
import warnings
import tempfile
import subprocess
from typing import Tuple
from pathlib import Path
from config import (
    TEST_FILE_NAME,
    TEST_TIMEOUT,
    SUBPROCESS_TIMEOUT,
    CUSTOM_PYTEST_CONFIG_PATH
)

FAILED_TESTS_PATTERN = (r"=+\s*FAILURES\s*=+\n"
                        r"(.*?)\n=+\s*short test summary info\s*=+")
TOTAL_COUNT_PATTERN = r"collected\s+(\d+)\s+items"
PASSED_COUNT_PATTERN = r"\s+(\d+)\s+passed in"


class TestRunner:
    def __init__(self, test_file: str, stop_on_fail: bool = False):
        self.tempdir = tempfile.TemporaryDirectory()
        self.work_dir = self.tempdir.name
        shutil.copy(
            test_file,
            os.path.join(self.work_dir, TEST_FILE_NAME))

        pytest_config = Path(__file__).resolve().parent / "conftest.py"
        if os.path.exists(CUSTOM_PYTEST_CONFIG_PATH):
            pytest_config = Path(CUSTOM_PYTEST_CONFIG_PATH)
        elif not os.path.exists(pytest_config):
            warnings.warn(f"{pytest_config} not found.")

        shutil.copy(pytest_config, os.path.join(self.work_dir, "conftest.py"))

        self.command = [
            sys.executable,
            "-m",
            "pytest",
            TEST_FILE_NAME,
            "--disable-warnings",
            "--no-header",
            "-vv",
            f"--timeout={TEST_TIMEOUT}",
            f"--rootdir={self.work_dir}",
            f"--basetemp={self.work_dir}/.pytest_tmp"
        ]
        if stop_on_fail:
            self.command.append("-x")

    def run_tests(self, code_str: str) -> Tuple[bool, str, Tuple[int, int]]:
        gen_func_path = os.path.join(self.work_dir, "generated_function.py")
        with open(gen_func_path, 'w') as f:
            f.write(code_str)

        env = {
            "TOKENIZERS_PARALLELISM": "false",
            "PYTHONPATH": "",
        }

        try:
            result = subprocess.run(
                self.command,
                cwd=self.work_dir,
                capture_output=True,
                text=True,
                env=env,
                timeout=SUBPROCESS_TIMEOUT
            )
        except subprocess.TimeoutExpired:
            return False, "Test execution timed out", (0, 0)

        if (result.stderr):
            raise RuntimeError(
                f"Unexpected error while testing:\n {result.stderr}")

        return (result.returncode == 0,
                self.__get_failures(result.stdout),
                self.__get_tests_count(result.stdout))

    def __get_failures(self, stdout: str) -> str:
        failure_match = re.search(FAILED_TESTS_PATTERN,
                                  stdout,
                                  re.DOTALL | re.IGNORECASE)
        return failure_match.group(1).strip() if failure_match else stdout

    def __get_tests_count(self, stdout: str) -> Tuple[int, int]:
        total_match = re.search(TOTAL_COUNT_PATTERN, stdout)
        total_tests = int(total_match.group(1)) if total_match else 0

        passed_matches = re.findall(PASSED_COUNT_PATTERN, stdout)
        return total_tests, int(passed_matches[-1]) if passed_matches else 0
