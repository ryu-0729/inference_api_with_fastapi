from requests import Response, request, exceptions


class RequestAPI:
    def __init__(self, access_token: str) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

    def request_post(
        self, url: str, payload: str
    ) -> Response | exceptions.RequestException:
        try:
            response = request(
                method="POST", url=url, headers=self.headers, data=payload
            )
            response.raise_for_status()
        except exceptions.RequestException as e:
            return e

        return response
