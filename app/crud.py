from sqlalchemy.orm import Session

from  models import User
from schemas import UserBase

def create_user(db: Session, user: UserBase):
    db_user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        age = user.age,
        gender = user.gender,
        pregnancies = user.pregnancies,
        glucose = user.glucose,
        blood_pressure = user.blood_pressure,
        skin_thickness = user.skin_thickness,
        insulin = user.insulin,
        bmi = user.bmi,
        dpf = user.dpf,
        result = user.result
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()