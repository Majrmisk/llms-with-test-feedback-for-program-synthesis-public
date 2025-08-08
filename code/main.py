import os
import io
from contextlib import redirect_stdout
from llm.llm_manager import LlmManager
from prompts.prompt_manager import PromptManager
from tester.test_runner import TestRunner
from cli.parser import parse_args
from config import MODEL_PATHS, RESTART_LIMIT


def iterate(iterations: int,
            llm_manager: LlmManager,
            prompt_manager: PromptManager,
            test_runner: TestRunner) -> None:

    last_passed = -1
    same_fail_count = 1
    prompt = prompt_manager.load_initial_prompt()
    initial_prompt = prompt

    for i in range(iterations):
        print(f"------- {i + 1}. ITERATION -------")

        response = llm_manager.generate_response(prompt)
        print(f"LLM RESPONSE\n{response}\n")

        code = prompt_manager.extract_code(response)
        if not code:
            print(f"{i + 1}. attempt failed - Failed to generate code")
            continue

        success, failures, (total, passed) = test_runner.run_tests(code)
        if success:
            return print(
                f"\nSuccessfully passed all tests after {i + 1} iterations:"
                f"\n{code}")

        if last_passed == passed:
            same_fail_count += 1
        else:
            same_fail_count = 1

        if same_fail_count >= RESTART_LIMIT:
            print(f"Failed the same amount of tests {RESTART_LIMIT}"
                  "times in a row. Restarting.")
            prompt = initial_prompt
            same_fail_count = 1
            last_passed = -1
            prompt_manager.reset_attempts()
            continue

        print(f"FAILED TESTS\n{failures}\n{passed} PASSED | {total} TOTAL")

        last_passed = passed
        prompt = prompt_manager.update_prompt(code, failures)

    print(f"\nFailed to generate working code after {iterations} iterations.")


def single_mode(prompt_file: str,
                test_file: str,
                iterations: int,
                stop_on_fail: bool,
                long_prompts: bool,
                llm_manager: LlmManager) -> None:

    prompt_manager = PromptManager(prompt_file, long_prompts)
    test_runner = TestRunner(test_file, stop_on_fail)

    iterate(iterations,
            llm_manager,
            prompt_manager,
            test_runner)


def folder_mode(folder_path: str,
                output_path: str,
                iterations: int,
                stop_on_fail: bool,
                long_prompts: bool,
                llm_manager: LlmManager) -> None:

    with open(output_path, "w") as output_file:
        for path, _, files in os.walk(folder_path):
            if "prompt.txt" not in files or "tests.py" not in files:
                continue

            folder_name = os.path.relpath(path, folder_path)
            print(f"Running: {folder_name}")

            output_file.write(
                f"================ {folder_name} ================\n")

            buffer = io.StringIO()
            try:
                with redirect_stdout(buffer):
                    single_mode(
                        os.path.join(path, "prompt.txt"),
                        os.path.join(path, "tests.py"),
                        iterations,
                        stop_on_fail,
                        long_prompts,
                        llm_manager
                    )
            except Exception as e:
                buffer.write("============== Error processing"
                             f" {folder_name}: {e} ==============\n")

            output_file.write(f"{buffer.getvalue()}\n\n")


def main(is_folder_mode: bool,
         file1: str,
         file2: str,
         iterations: int,
         model_path: str,
         stop_on_fail: bool,
         long_prompts: bool) -> None:

    mode_fn = folder_mode if is_folder_mode else single_mode
    mode_fn(file1,
            file2,
            iterations,
            stop_on_fail,
            long_prompts,
            LlmManager(model_path))


if __name__ == "__main__":
    # Needs to be set to avoid warnings when running a subprocess
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    args = parse_args()

    main(args.folder,
         args.file1,
         args.file2,
         args.iterations,
         MODEL_PATHS[args.model],
         args.exitfirst,
         args.longprompt)
