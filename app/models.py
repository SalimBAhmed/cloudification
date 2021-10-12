from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Float, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index= True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    gender = Column(Integer)
    pregnancies = Column(Integer)
    glucose = Column(Float)
    blood_pressure = Column(Float)
    skin_thickness = Column(Float)
    insulin = Column(Float)
    bmi = Column(Float)
    dpf = Column(Integer)
    result = Column(Integer)




















    
