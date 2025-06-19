def format_linter_error(error: dict) -> dict:
    # write your code here
    return {"line": error["line-number"],
            "column": error["column_number"],
            "message": error["text"],
            "name": error["code"],
            "source": "flake8"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    return {"errors": [format_linter_error(error) for error in errors], "path": file_path, "status": "pass" if not errors else "failed"}


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    return [format_single_linter_file(list(linter_report.keys())[0], []),
            format_single_linter_file(list(linter_report.keys())[1], linter_report[list(linter_report.keys())[1]])]
