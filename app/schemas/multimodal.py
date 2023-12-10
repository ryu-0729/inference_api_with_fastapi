from pydantic import Field

from app.utils.custombasemodel import CustomBaseModel


class ImageToTextRequest(CustomBaseModel):
    image_url: str = Field(..., description="画像URL")


class ImageToTextResponse(CustomBaseModel):
    image_to_text: str = Field(..., description="生成されたテキスト")
