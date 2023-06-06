import threading
import time
import os
import shutil

def delete_folder(folder_path: str, timeout: int):
    time.sleep(timeout)
    if existsImageDirectoryOrCreate():
        shutil.rmtree(folder_path)

def working(file_path: str):
    thread = threading.Thread(target=delete_folder, args=(file_path, 10*60)) # 10 minutes
    thread.start()