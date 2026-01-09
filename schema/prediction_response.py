from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str = Field(
        ..., 
        description="The predicted insurance premium category",
        example="High"
    )
    confidence:float = Field(
        ..., 
        description="Confidence score of predicted class (0 to 1)"
    )
    class_probabilities:Dict[str,float] = Field(
        ...,
        description="Probability distribution across all classes"
    )