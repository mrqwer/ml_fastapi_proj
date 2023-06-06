import os

DIRECTORY_PATH = "./model/imgs"

def existsAnyFile() -> bool:
    return any(os.listdir(DIRECTORY_PATH))
def existsImageDirectoryOrCreate(create: bool=False) -> bool:
    if not os.path.exists(DIRECTORY_PATH):
        if create:
            os.makedirs(DIRECTORY_PATH)
        return False
    return True

    