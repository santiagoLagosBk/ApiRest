#Python
from typing import Optional

#Model
from models.person import Person
from models.person import Person_out
from models.loginOut import LoginOut,Login
 
# Pydantic
from pydantic import EmailStr

#Service
from services.person_service import Person_src


#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile
from fastapi import status




app = FastAPI()

@app.get("/")
def run():
    return {"Hello World":"Arley Santiago"} 


@app.get("/Home")
def home():
    return [{"name":"santiago"},{"name":"mateo"}]



# Request and Response Body

@app.post("/signup",response_model = Person_out,status_code = status.HTTP_201_CREATED)
def create_person(person : Person = Body(...)):
    service = Person_src()
    service.save_person(person.to_dict())
    
    return person

# Validation Query Paramenters

@app.get("/users",status_code = status.HTTP_200_OK)
def get_users(user_name : Optional[str] = Query(
    None,
    min_length = 1,
    max_length = 30,
    example = "Enrique")
    ):

    """This method bring The json user if the parameter 
       is None will bring you the list all of them  """
    
    service = Person_src()
        
    return service.read_person(user_name)
    

# Validation Path Paramenter

@app.get("/users/{user_name}")
def topppics_in_common(user_name:str = Path(
    ...,
    min_length = 1,
    max_length = 18
    )
    ):

    """This method will bring you all of the other 
        users you that share a topic of you like and
        will recommend it to you"""
    
    service = Person_src()
    return service.recomend_who_follow(user_name)

# Forms
@app.post(path = "/login",response_model = LoginOut,status_code = status.HTTP_200_OK)
def login(username:str = Form(...), password:str = Form(...,max_length = 12)):
    
    login = Login(username = username,password = password)
    print(login.dict())
    return LoginOut(username = username)
    

# Cookies and Headers
@app.post(path = "/contact",status_code = status.HTTP_200_OK)
def contact(first_name:str = Form(
    ...,
    max_length = 20,
    min_length = 2),
    email: EmailStr = Form(...),
    message:str = Form(...,
    min_length = 20),
    user_agent:Optional[str] = Header(default=None),
    ads:Optional[str] = Cookie(default=None)
    ):
    
    return user_agent

@app.post(path = "/post-image")
def post_image(image: UploadFile = File(...)):
    return {
        "File name":image.filename,
        "Format":image.content_type,
        "File size (Kb)":round(len(image.file.read())/1024,2)
    }
