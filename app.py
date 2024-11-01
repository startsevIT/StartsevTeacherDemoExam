import datetime
from pydantic import BaseModel


class Order(BaseModel):
    number : int
    startDate: datetime.date
    device : str
    problemType : str
    description : str
    client : str
    status : str


from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return "Hello"