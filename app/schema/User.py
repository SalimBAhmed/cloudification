from sqlalchemy import table,Column
from sqlalchemy.sql.sqltypes import Integer,Float,String

users=table(
    'users',meta,
    Column('id', Integer, primary_key=True),
    Column('first_name',String),
    Column('last_name', String),
    Column('age',Integer),
    Column('gender', Integer),
    Column('pregnancies', Integer),
    Column('glucose', Float),
    Column('blood_pressure', Float),
    Column('skin_thickness', Float),
    Column('insulin', Float),
    Column('bmi', Float),
    Column('dfp', Float),
    Column('resultat', String(255)),
    )