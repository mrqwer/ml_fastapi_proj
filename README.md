# ML integrated Web Service on FastAPI task

## Run Locally
To run the service. Do the following:

Create directory
```bash
touch folder_name
```

Go to the folder_name
```bash
cd folder_name
```

Create virtual environment
```bash
python3 -m venv venv
```
Get inside 
```bash
source venv/bin/activate
```
Clone the project
```bash
git clone git@github.com:mrqwer/ml_fastapi_proj.git
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the service
```bash
uvicorn main:app --reload
```

## Go to the Documentation
http://127.0.0.1:8000/docs

## To perform testing, run
```bash
pytest main.py
```

## API endpoints
- /upload - for uploading multiple image files
- /predict - for predicting previous uploaded images based on pretrained ResNet50 model.