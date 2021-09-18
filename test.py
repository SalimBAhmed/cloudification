# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:25:45 2021

@author: najeh
"""


from fastapi import FastAPI

import pickle

m=pickle.load(open('model1','rb'))

app=FastAPI()
user=APIRouter()
@app.get("/")
async def hello_world():
    return {"hello":"world22"}

@app.get('/items/{name}')
async def get_items(name):
    return {"name":name}
@app.get('/predict/{name}')
async def predict(name,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
   
   pr=int(Pregnancies) 
   Gl=int(Glucose)
   Bl=int(BloodPressure)
   Sk=int(SkinThickness)
   In=int(Insulin)
   BM=int(BMI)
   Di=int(DiabetesPedigreeFunction)
   Ag=int(Age)
   x=[pr,Gl,Bl,Sk,In,BM,Di,Ag]
   x1=[x]
   pre=m.predict(x1)
   if pre[0]==0:
       ch="no"
   else:
       ch="yes"
   return {"prediction":ch}