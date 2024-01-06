import json

from fastapi import APIRouter, Depends

from app.core.config import settings
from app.core.requestapi import RequestAPI
from app.schemas.text import (
    TextClassificationRequest,
    TextClassificationResponse,
    QuestionAnswerRequest,
    QuestionAnswerResponse,
)

router = APIRouter()

request_api = RequestAPI(access_token=settings.HUGGING_FACE_ACCESS_TOKEN)


@router.get("/text-classification", description="テキストから感情分析するAPI")
def text_classification(
    req: TextClassificationRequest = Depends(),
) -> TextClassificationResponse:
    url = "https://api-inference.huggingface.co/models/SamLowe/roberta-base-go_emotions"
    payload = json.dumps({"text": req.text})
    api_response = request_api.request_post(url=url, payload=payload)

    response = TextClassificationResponse(
        textClassification=json.loads(api_response.text)
    )
    return response


@router.get("/question-answer", description="テキストの問題に答えるAPI")
def question_answer(
    req: QuestionAnswerRequest = Depends(),
) -> QuestionAnswerResponse:
    url = (
        "https://api-inference.huggingface.co"
        "/models/IProject-10/xlm-roberta-base-finetuned-squad2"
    )
    payload = json.dumps({"inputs": {"question": req.question, "context": req.context}})
    api_response = request_api.request_post(url=url, payload=payload)

    response = QuestionAnswerResponse(questionAnswer=json.loads(api_response.text))

    return response
