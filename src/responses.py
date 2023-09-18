from pydantic import BaseModel


class Success(BaseModel):
    status_code: int = 200
    message: str = "success"


class BaseError(BaseModel):
    status_code: int = 500
    message: str = "Internal Server Error"
    error_code: int = 0


class UnsupportedMediaType(BaseError):
    status_code: int = 415
    message: str = "Unsupported Media Type"
    error_code: int = 0


class RequestEntityTooLarge(BaseError):
    status_code: int = 413
    message: str = "Request Entity Too Large"
    error_code: int = 0


class EmptyFileUpload(BaseError):
    status_code: int = 400
    message: str = "Empty File Upload"
    error_code: int = 0


class FileUpload(BaseError):
    status_code: int = 400
    message: str = "File Upload Failed"
    error_code: int = 0
