from http import HTTPStatus

from requests.models import Response


class ClientException(Exception):
    def __init__(
        self,
        response: Response,
    ):
        super().__init__()
        self.response = response
        print(f"[{response.status_code} - {HTTPStatus(response.status_code).name}]: {response.content}")
