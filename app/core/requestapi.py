from requests import Response, request, exceptions

from fastapi import HTTPException


class RequestAPI:
    def __init__(self, access_token: str) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}",
        }

    def request_post(self, url: str, payload: str) -> Response:
        try:
            response = request(
                method="POST", url=url, headers=self.headers, data=payload
            )
            response.raise_for_status()
        except exceptions.RequestException:
            raise HTTPException(
                status_code=500,
                detail="APIエラーです。しばらく時間を置いてから再度実行してください。",
            )

        return response
