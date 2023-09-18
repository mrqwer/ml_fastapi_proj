from pydantic import BaseModel, Field
from typing import List

example = [
    {
        "top": 1,
        "description": "Persian_cat",
        "probability": "85.38%"
    },
    {
        "top": 2,
        "description": "hamper",
        "probability": "1.54%"
    }
]


class Label(BaseModel):
    top: int = Field(..., description="Top k number outcome")
    description: str = Field(..., description="Name class of the outcome")
    probability: str = Field(..., description="Probability of a class")

    class Config:
        json_schema_extra = example[0]


class Predictions(BaseModel):
    image_number: int = Field(..., description="Image number")
    prediction: List[Label] = Field(..., description="A list of labels' predictions")

    class Config:
        json_schema_extra = {
            "image_number": 1,
            "prediction": example
        }
