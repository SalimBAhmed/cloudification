from sqlalchemy.orm.session import Session
from database import SessionLocal, engine

from re import template
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pickle

import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
#app.mount("public/css", StaticFiles(directory="/public/css"), name="css")
templates = Jinja2Templates(directory="public/")

model = pickle.load(open('/cloudification/app/model1','rb'))

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})

@app.post("/", response_class=HTMLResponse)
def check(
    request: Request,
    db: Session = Depends(get_db),
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
    dpf: int = Form(...)
    ):
    
    #({"first_name": first_name, "last_name": last_name, "age": age, "gender": gender})
    
    bmi = weight/((height/100)**2)
    x = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
    prediction = model.predict(x)

    user = schemas.UserBase(
        first_name= first_name, 
        last_name= last_name, 
        age= age, 
        gender= gender, 
        pregnancies= pregnancies, 
        glucose= glucose, 
        blood_pressure= blood_pressure, 
        skin_thickness= skin_thickness, 
        insulin= insulin, 
        bmi= bmi, 
        dpf= dpf, 
        result= prediction
    )
    crud.create_user(db, user)

    #return [first_name, last_name, gender, x]
    result = "You are fine! but checking the doctor once in a while won't hurt ;)"
    if( prediction ) :
        result = "You might have diabetes :o ! Please check the doctor immediately!"
    return templates.TemplateResponse("result.html", context={'request': request, 'result': result})

@app.get("/user/{id}")
def read_user(id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, id)
