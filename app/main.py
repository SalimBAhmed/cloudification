from re import template
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.sql.functions import user

import pickle

from model.User import User

app = FastAPI()

app.mount("/public/css", StaticFiles(directory="public/css"), name="css")
templates = Jinja2Templates(directory="public/")

model = pickle.load(open('model1','rb'))

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})

@app.post("/")
def check(request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    age: int = Form(...),
    gender: int = Form(...),
    pregnancies: int = Form(...), 
    glucose: float = Form(...),
    blood_pressure: float = Form(...),
    skin_thickness: float = Form(...),
    insulin: float = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    dpf: float = Form(...)
    ):
    
    #({"first_name": first_name, "last_name": last_name, "age": age, "gender": gender})
    
    bmi = weight/((height/100)**2)
    x = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
    prediction = model.predict(x)
    #return [first_name, last_name, gender, x]
    result = False
    if( prediction ) :
        result = True
    return templates.TemplateResponse("result.html", context={'request': request, 'result': result})