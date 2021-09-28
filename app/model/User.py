from pydantic import BaseModel

class User(BaseModel):
    first_name : str
    last_name : str
    age : int
    gender: int
    pregnancies: int = 0
    glucose: float = 0
    blood_pressure: float = 0
    skin_thickness: float = 0
    insulin: float = 0
    bmi: float = 0 
    dpf: float = 0
    result: str = "Good"