from typing import Any

from pydantic import Field

from app.utils.custombasemodel import CustomBaseModel


class TextClassificationRequest(CustomBaseModel):
    text: str = Field(..., description="感情分析するテキスト")


class TextClassificationResponse(CustomBaseModel):
    text_classification: list[dict[str, Any]] = Field(..., description="感情分析結果")


class QuestionAnswerRequest(CustomBaseModel):
    question: str = Field(..., description="問題文")
    context: str = Field(..., description="文章")


class QuestionAnswerResponse(CustomBaseModel):
    question_answer: dict[str, Any] = Field(..., description="回答")
