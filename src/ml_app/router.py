from typing import List

from fastapi import APIRouter, UploadFile, File

from .ml import get_model_predictions
from .service import existsImageDirectoryOrCreate, existsAnyFile, upload_files
from .worker import working
from ..responses import Success
from ..dependencies import get_exception_responses
from ..exceptions import UnsupportedMediaTypeException, RequestEntityTooLargeException, \
                         EmptyFileUploadException, FileUploadException, BaseAPIException
from ..config import UPLOAD_FOLDER
router = APIRouter(prefix='/ml', tags=["ml"])


@router.get(
    "/predict",
    response_model=dict,
    responses=get_exception_responses(EmptyFileUploadException)
)
async def predict():
    try:
        if not existsImageDirectoryOrCreate(create=True):
            working(UPLOAD_FOLDER)

        existsAnyFile()

        predictions = get_model_predictions()
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
