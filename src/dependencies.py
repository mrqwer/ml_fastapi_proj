from typing import Type
from fastapi import UploadFile
import magic
from .config import MAX_IMAGE_UPLOAD_SIZE, ALLOWED_MEDIA_TYPES
from .exceptions import BaseAPIException, RequestEntityTooLargeException, \
    EmptyFileUploadException, UnsupportedMediaTypeException


def get_exception_responses(*exceptions: Type[BaseAPIException]) -> dict:
    responses = dict()
    for exception in exceptions:
        responses.update(exception.response_model())
    return responses


def validate_file_size(file: UploadFile):
    if file.size > MAX_IMAGE_UPLOAD_SIZE:
        raise RequestEntityTooLargeException


def validate_emptiness(files: list[UploadFile]):
    if not len(files):
        raise EmptyFileUploadException


def validate_file_format(file: UploadFile):
    file_type = magic.from_buffer(file.file.read(2048), mime=True)
    if file_type not in ALLOWED_MEDIA_TYPES:
        raise UnsupportedMediaTypeException

# def validate_file_format(file: UploadFile):
#     # Open the file in binary mode to read its content
#     with file.file as f:
#         # Read the first 2048 bytes of the file to determine its type
#         file_data = f.read(2048)
#
#     # Determine the MIME type of the file using magic_bin
#     file_type = magic.Magic()
#     detected_mime_type = file_type.from_buffer(file_data, mime=True)
#
#     # Check if the detected MIME type is in the list of allowed types
#     if detected_mime_type not in ALLOWED_MEDIA_TYPES:
#         raise UnsupportedMediaTypeException