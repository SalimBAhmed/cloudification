# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:19:50 2021

@author: najeh
"""

from sqlalchemy import table,Column
from sqlalchemy.sql.sqltypes import Integer,Float,String
from configuration.db import meta

users=table(
    'users',meta,
    Column('Nom',String,primary_key=True),
    Column('Pregnancies',Integer),
    Column('Glucose',Integer),
    Column('BloodPressure',Integer),
    Column('SkinThickness',Integer),
    Column('Insulin',Integer),
    Column('BMI',Integer),
    Column('Insulin',Integer),
    Column('DiabetesPedigreeFunction',Integer),
    Column('Age',Integer),
    Column('Résultat',String(255)),
    )