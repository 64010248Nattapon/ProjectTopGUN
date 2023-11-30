from typing import Optional
from pydantic import BaseModel, Field


class WaterSchema(BaseModel):
    # Name: str= Field(...)
    # Year: int = Field(..., gt=1990, lt=2030)
    station_id: int = Field(..., gt=0, lt=100)
    Date: int = Field(..., gt=0,)
    # Month: int = Field(..., gt=0, lt=13)
    w_height: float = Field(..., ge=01.0)
    w_discharge: float = Field(..., ge=0.0)
    # WaterDrainRate: float = Field(..., ge=0.0)  

    class Config:
        schema_extra = {
            "example": {
                # "Name":"huu",
                # "Year": 2020,
                # "Month":12,
                "station_id": 1,
                "Date":51,
                "w_height":121.1,
                "w_discharge":111.3,
                # "WaterDrainRate":111.3
            }
        }

class UpdateWaterModel(BaseModel):
    # Name: Optional[str]
    # Year: Optional[int]
    station_id: Optional[int]
    Date: Optional[int]
    # Month: Optional[int]
    w_height: Optional[float]
    w_discharge: Optional[float]
    # WaterDrainRate: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                # "Name":"huu",
                "station_id": "1",
                "Date":51,
                "w_height":121.1,
                "w_discharge":111.3,
            }
        }
    



def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
    
# give me function post

