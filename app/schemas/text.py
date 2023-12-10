from typing import Any

from pydantic import Field

from app.utils.custombasemodel import CustomBaseModel


class TextClassificationRequest(CustomBaseModel):
    text: str = Field(..., description="感情分析するテキスト")


class TextClassificationResponse(CustomBaseModel):
    text_classification: list[dict[str, Any]] = Field(..., description="感情分析結果")
