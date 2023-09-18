from typing import List
from fastapi import UploadFile
import os
import shutil
from ..exceptions import EmptyFileUploadException, FileUploadException
from ..config import UPLOAD_FOLDER
from ..dependencies import validate_file_size, validate_emptiness, validate_file_format

DIRECTORY_PATH = "imgs"


def existsAnyFile() -> None:
    if not any(os.listdir(DIRECTORY_PATH)):
        raise EmptyFileUploadException


def existsImageDirectoryOrCreate(create: bool = False) -> bool:
    if not os.path.exists(DIRECTORY_PATH):
        if create:
            os.makedirs(DIRECTORY_PATH)
        return False
    return True


def upload_files(files: List[UploadFile]) -> None:
    validate_emptiness(files)
    for file in files:
        validate_file_size(file)
        validate_file_format(file)
    for i, img in enumerate(files):
        filepath = os.path.join(UPLOAD_FOLDER, img.filename)
        with open(filepath, "wb") as buffer:
            img.file.seek(0)
            shutil.copyfileobj(img.file, buffer)
        if not os.path.exists(filepath):
            raise FileUploadException
