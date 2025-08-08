# Main loop
BASE_ITERATION_LIMIT = 10
RESTART_LIMIT = 3

# Testing
CUSTOM_PYTEST_CONFIG_PATH = ""
TEST_FILE_NAME = "tests.py"
TEST_TIMEOUT = 20
SUBPROCESS_TIMEOUT = 10 * TEST_TIMEOUT

# LLMs
MODEL_PATHS = [
    "/data/xnadzam/llms/Qwen/Qwen2.5-Coder-3B-Instruct",
    "/data/xnadzam/llms/Qwen/Qwen2.5-Coder-7B-Instruct",
    "/data/xnadzam/llms/Qwen/Qwen2.5-Coder-32B-Instruct",
]
LLM_MAX_NEW_TOKENS = 4096
