import json

from fastapi import APIRouter, Depends

from app.core.config import settings
from app.core.requestapi import RequestAPI
from app.schemas.multimodal import ImageToTextRequest, ImageToTextResponse

router = APIRouter()

request_api = RequestAPI(access_token=settings.HUGGING_FACE_ACCESS_TOKEN)


@router.get("/image-to-text", description="画像からテキストを生成するAPI")
def image_to_text(req: ImageToTextRequest = Depends()) -> ImageToTextResponse:
    url = (
        "https://api-inference.huggingface.co/models/"
        "Salesforce/blip-image-captioning-large"
    )
    payload = json.dumps({"inputs": req.image_url})
    api_response = request_api.request_post(url=url, payload=payload)

    response = ImageToTextResponse(
        imageToText=json.loads(api_response.text)[0]["generated_text"]
    )

    return response
