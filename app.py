import datetime
from pydantic import BaseModel
from fastapi import FastAPI

class Order(BaseModel):
    number : int
    startDate: datetime.date
    device : str
    problemType : str
    description : str
    client : str
    status : str

repo = []

 
app = FastAPI()
 
@app.get("/")
def read_root():
    return "Hello"