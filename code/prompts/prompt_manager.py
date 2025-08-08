import re
import textwrap
from prompts.main_prompts import (
    INITIAL_PROMPT,
    REFINEMENT_PROMPT
)


PROMPT_TESTS_LONG = (
    "Previously generated code and its corresponding failed tests. "
    "(sorted from the first iteration to the latest attempt):\n"
    "{tests}\n\n"
)

PROMPT_TESTS_SHORT = (
    "Previously generated Code:\n{code}\n\n"
    "Failed Tests or Errors:\n{tests}\n\n"
)

ATTEMPT_SUMMARY = (
    "============== Iteration {iteration} ===============\n"
    "\n"
    "Code:\n"
    "{code}\n"
    "\n"
    "Failed Tests or Errors:\n"
    "{failures}\n"
)

EXTRACT_CODE_PATTERN = r"^\s*```python\s*\n(.*?)\n\s*```"


class PromptManager:
    def __init__(self, prompt_file: str, long_prompts: bool):
        self.prompt_file = prompt_file
        self.user_input = ""
        self.attempts = []
        self.iteration = 0
        self.long_prompts = long_prompts

    def load_initial_prompt(self) -> str:
        try:
            with open(self.prompt_file, 'r') as file:
                self.user_input = file.read().strip()
                if not self.user_input:
                    raise ValueError(
                        f"Prompt file '{self.prompt_file}' is empty.")
                return INITIAL_PROMPT.format(user_input=self.user_input)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Prompt file '{self.prompt_file}' not found.")
        except Exception as e:
            raise RuntimeError(f"Error reading prompt file: {e}")

    def extract_code(self, response: str) -> str:
        matches = re.findall(
            EXTRACT_CODE_PATTERN,
            response,
            re.DOTALL | re.MULTILINE)
        dedented_code_blocks = [
            textwrap.dedent(match).strip()
            for match in matches if "def " in match
        ]
        return "\n\n".join(dedented_code_blocks)

    def update_prompt(self,
                      previous_code: str,
                      fails_output: str) -> str:
        if self.long_prompts:
            return self.__create_failed_test_prompt_long(previous_code,
                                                         fails_output)
        return self.__create_failed_test_prompt_short(previous_code,
                                                      fails_output)

    def reset_attempts(self) -> None:
        self.attempts = []
        self.iteration = 0

    def __create_failed_test_prompt_long(
            self,
            current_code: str,
            fails_output: str) -> str:
        self.__add_attempt(current_code, fails_output)
        return REFINEMENT_PROMPT.format(
            user_input=self.user_input,
            tests=PROMPT_TESTS_LONG.format(tests="\n".join(self.attempts))
        )

    def __create_failed_test_prompt_short(
            self,
            previous_code: str,
            fails_output: str) -> str:
        return REFINEMENT_PROMPT.format(
            user_input=self.user_input,
            tests=PROMPT_TESTS_SHORT.format(
                code=previous_code,
                tests=fails_output
            )
        )

    def __add_attempt(self,
                      code: str,
                      fails_output: str) -> None:
        self.iteration += 1
        attempt_summary = ATTEMPT_SUMMARY.format(
            iteration=self.iteration,
            code=code,
            failures=fails_output or "None"
        )
        self.attempts.append(attempt_summary)
