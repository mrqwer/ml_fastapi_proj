from typing import List

from fastapi import APIRouter, UploadFile, File, Query

from .ml import get_model_predictions
from .service import existsImageDirectoryOrCreate, existsAnyFile, upload_files
from .worker import working
from .models import Predictions
from ..responses import Success
from ..dependencies import get_exception_responses
from ..exceptions import UnsupportedMediaTypeException, RequestEntityTooLargeException, \
                         EmptyFileUploadException, FileUploadException, BaseAPIException
from ..config import UPLOAD_FOLDER
router = APIRouter(prefix='/ml', tags=["ml"])


@router.get(
    "/predict",
    response_model=List[Predictions],
    responses=get_exception_responses(EmptyFileUploadException)
)
async def predict(top: int = Query(default=1, gt=0, lt=6)):
    try:
        if not existsImageDirectoryOrCreate(create=True):
            working(UPLOAD_FOLDER)

        existsAnyFile()

        predictions = get_model_predictions(top)
    except BaseAPIException as e:
        raise e
    return predictions


@router.post(
    "/upload",
    response_model=Success,
    responses=get_exception_responses(UnsupportedMediaTypeException, RequestEntityTooLargeException,
                                      EmptyFileUploadException, FileUploadException)
)
async def upload_image(files: List[UploadFile] = File(...)):
    try:
        if not existsImageDirectoryOrCreate(create=True):
            working(UPLOAD_FOLDER)

        upload_files(files)
    except BaseAPIException as e:
        raise e
    return Success()
