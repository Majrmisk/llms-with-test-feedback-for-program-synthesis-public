import pytest

MAX_TRACEBACK_ENTRIES = 5
MAX_TRACEBACK_LINES = 40


def pytest_exception_interact(node, call, report):
    tb = getattr(report.longrepr, "reprtraceback", None)
    if tb and hasattr(tb, "reprentries"):
        entries = tb.reprentries
        if len(entries) > MAX_TRACEBACK_ENTRIES + 1:
            tb.reprentries = [entries[0]] + entries[-MAX_TRACEBACK_ENTRIES:]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        truncate_traceback(report)
    return report


def truncate_traceback(report):
    tb = getattr(report.longrepr, "reprtraceback", None)
    if not tb or not tb.reprentries:
        return
    last_entry = tb.reprentries[-1]
    if len(last_entry.lines) > MAX_TRACEBACK_LINES:
        last_entry.lines = transform_last_entry_lines(last_entry.lines)


def transform_last_entry_lines(lines):
    return lines[:1] + ["        ......"] + lines[-MAX_TRACEBACK_LINES:]
