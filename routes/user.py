# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:37:45 2021

@author: najeh
"""

from fastapi import APIRouter
from configuration.db import conn
from models.index import users 
import schemas.index import User 

user=APIRouter()

@user.post("/")
async def write_data(user:User):
    conn.execute(users.insert().values(
        name=user.name,
        Pregnancies=user.Pregnancies
        Glucose=user.Glucose
        BloodPressure=user.BloodPressure
        SkinThickness=user.SkinThickness
        Insulin=user.Insulin
        BMI=user.BMI
        DiabetesPedigreeFunction=user.DiabetesPedigreeFunction
        Age=user.Age
        resultat=user.resultat))
     return conn.execute (users.select()).fetchall()