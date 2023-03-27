from http import HTTPStatus


def abort(status_code: int, detail: str):
    print(f"[{status_code} - {HTTPStatus(status_code).name}]: {detail}")
    return None
