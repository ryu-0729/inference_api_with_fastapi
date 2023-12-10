import json

from fastapi import APIRouter, Depends

from app.core.config import settings
from app.core.requestapi import RequestAPI
from app.schemas.text import TextClassificationRequest, TextClassificationResponse

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
