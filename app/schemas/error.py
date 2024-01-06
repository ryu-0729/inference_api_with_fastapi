from pydantic import Field

from app.utils.custombasemodel import CustomBaseModel


class ApiErrorResponse(CustomBaseModel):
    error_message: str = Field(..., description="エラーメッセージ")
