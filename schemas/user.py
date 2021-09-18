from pydantic import BaseModel
      
class User(BaseModel):
     nom:str
     Pregnancies:int
     BloodPressure:int
     SkinThickness:int
     Insulin:int
     BMI:int
     DiabetesPedigreeFunction:int
     Age:int
     resultat:str