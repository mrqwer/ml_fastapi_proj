import uvicorn
import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

from model.helpers import existsImageDirectoryOrCreate, existsAnyFile
from model.model import get_model_predictions

import os
from typing import List, Union

from worker import working

app = FastAPI(debug=True)

UPLOAD_FOLDER = "./model/imgs"

@app.post("/upload")
async def upload_image(files: List[UploadFile] = File(...)):
    if not existsImageDirectoryOrCreate(create=True):
        working(UPLOAD_FOLDER)
    response = []
    for i, img in enumerate(files):
        filepath = os.path.join(UPLOAD_FOLDER, img.filename)
        try:
            with open(filepath, "wb") as buffer:
                shutil.copyfileobj(img.file, buffer)
            if os.path.exists(filepath):
                response.append({'Image': i+1, "message": "File uploaded successfully"})
            else:
                response.append({"Image": i+1, "message": "Failed to save file"})
        except Exception as e:
            response.append({"Image": i+1, "message": f"Failed to process file: {str(e)}"})
    
    if len(files) == 1:
        return response[0]
    
    return response

@app.get("/predict")
async def predict():
    if not existsImageDirectoryOrCreate(create=True):
        working(UPLOAD_FOLDER)
    if not existsAnyFile():
        return {"message": "Please, firstly upload images"}

    predictions = get_model_predictions()
    print(predictions)
    return predictions

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



