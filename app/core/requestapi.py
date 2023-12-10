from requests import Response, request


class RequestAPI:
    def __init__(self, access_token: str) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

    def request_post(self, url: str, payload: str) -> Response:
        return request(method="POST", url=url, headers=self.headers, data=payload)
