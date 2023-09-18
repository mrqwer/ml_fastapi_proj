from .responses import BaseError, UnsupportedMediaType, RequestEntityTooLarge, EmptyFileUpload, FileUpload


class BaseAPIException(Exception):
    status_code: int = 500
    message: str = "Internal Server Error"
    model = BaseError

    @classmethod
    def response_model(cls) -> dict:
        js_response = {
            cls.status_code: {"model": cls.model, "description": cls.message}
        }
        return js_response


class UnsupportedMediaTypeException(BaseAPIException):
    status_code: int = 415
    message: str = "Unsupported media type"
    model = UnsupportedMediaType


class RequestEntityTooLargeException(BaseAPIException):
    status_code: int = 413
    message: str = "Request payload is too large"
    model = RequestEntityTooLarge


class EmptyFileUploadException(BaseAPIException):
    status_code: int = 400
    message: str = "Bad Request"
    model = EmptyFileUpload


class FileUploadException(BaseAPIException):
    status_code: int = 400
    message: str = "Bad Request"
    model = FileUpload
