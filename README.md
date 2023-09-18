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

Run the service in a container
```bash
docker compose up
```

## Go to the Documentation
Try to upload png images and get the predictions of them
http://127.0.0.1:8000/docs
## API Reference

#### Post a list of files through http multipart/form-data

```http
  POST /ml/upload/
```
#### Get predictions of uploaded files

```http
  GET /ml/predict/?top={top}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `top`     | `int`    | Get top k predictions. default=1  |

