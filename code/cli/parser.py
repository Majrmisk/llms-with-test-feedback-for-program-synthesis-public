import argparse
from config import BASE_ITERATION_LIMIT, MODEL_PATHS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=(
        "Iteratively generates Python code based on the provided prompt"
        " and tests until all tests pass or an iteration limit is reached."))

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "-f", "--folder",
        dest="mode",
        action="store_const",
        const="folder",
        help=(
            "Folder mode - interpret positional args as "
            "<folder> <output_file>. \n"
            "Scans all subdirectories of <folder> for "
            "`prompt` and `tests` files "
            "and outputs the results to <output_file>."
        )
    )
    mode_group.add_argument(
        "-s", "--single",
        dest="mode",
        action="store_const",
        const="single",
        help=(
            "Single mode (default) - interpret positional args as "
            "<prompt_file> <test_file>."
        )
    )
    parser.set_defaults(mode="single")

    parser.add_argument(
        "-m", "--model",
        type=__validate_model_index,
        default=1,
        help=(
            "Index of the model from config/main_config.py to use."
        )
    )

    parser.add_argument(
        "-i", "--iterations",
        type=__validate_iterations,
        default=BASE_ITERATION_LIMIT,
        help=(f"Max number of failed iterations ({BASE_ITERATION_LIMIT} "
              "before the program is stopped).")
    )

    parser.add_argument(
        "-l", "--longprompt",
        action="store_true",
        help="Include all failed iterations in prompts."
    )
    parser.add_argument(
        "-x", "--exitfirst",
        action="store_true",
        help="Stop test execution after the first failed test."
    )

    parser.add_argument(
        "file1",
        help="Single mode: prompt file path. Folder mode: folder path."
    )
    parser.add_argument(
        "file2",
        help="Single mode: test file path. Folder mode: output file path."
    )

    return parser.parse_args()


def __validate_iterations(value: str) -> int:
    ivalue = int(value)
    if 1 <= ivalue <= BASE_ITERATION_LIMIT:
        return ivalue
    raise argparse.ArgumentTypeError(
        f"Iterations must be between 1 and {BASE_ITERATION_LIMIT}.")


def __validate_model_index(val: str) -> int:
    try:
        i = int(val)
    except ValueError:
        raise argparse.ArgumentTypeError("Model index must be an integer.")
    if not (0 <= i < len(MODEL_PATHS)):
        raise argparse.ArgumentTypeError(
            ("Model index must be an integer between "
             f"0 and {len(MODEL_PATHS)-1}, got {i}")
        )
    return i
