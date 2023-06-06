from fastapi.testclient import TestClient
from .main import app
import pytest


DIRECTORY_FOR_TEST = "./images"

client = TestClient(app)

def test_predict():
    response = client.get('/predict')
    assert response.status_code == 200
    assert 'predictions' in response.json()


def test_upload_image():

    files = [
        ('files', ('cat1.png', open(os.path.join(DIRECTORY_FOR_TEST, "cat1.png"), 'rb'), 'image/png')),
        ('files', ('cat2.png', open(os.path.join(DIRECTORY_FOR_TEST, "cat2.png"), 'rb'), 'image/png')),
        ('files', ('dog.png', open(os.path.join(DIRECTORY_FOR_TEST, "dog.png"), 'rb'), 'image/png')),
        ('files', ('dog1.png', open(os.path.join(DIRECTORY_FOR_TEST, "dog1.png"), 'rb'), 'image/png')),
    ]
    response = client.post('/upload', files=files)
    assert response.status_code == 200
    assert response.json()["message"] == {'message': 'File uploaded successfully'}

test_upload_image()

test_predict()
