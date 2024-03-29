from http import HTTPStatus

from requests.models import Response


class ClientException(Exception):
    def __init__(
        self,
        response: Response,
        method="GET",
    ):
        super().__init__()
        self.response = response
        print(
            f"{method} {response.url} - [{response.status_code} - {HTTPStatus(response.status_code).name}]: "
            f"{str(response.content)}",
        )
