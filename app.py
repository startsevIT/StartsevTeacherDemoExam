import datetime
from typing import Annotated, Optional
from pydantic import BaseModel
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

class Order(BaseModel):
    number : int
    startDate: datetime.date
    device : str
    problemType : str
    description : str
    client : str
    status : str
    master : Optional[str] = "Не назначен"

class UpdateOrderDTO(BaseModel):
    number: int
    status: Optional[str] = ""
    description: Optional[str] = ""
    master: Optional[str] = ""

repo = [
    Order(
        number = 1,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    ),
    Order(
        number = 2,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    ),
    Order(
        number = 3,
        startDate = "2000-12-01",
        device = "123",
        problemType = "123",
        description = "123",
        client = "123",
        status = "в ожидании"
    )
]

app = FastAPI()
 
app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_methods = ["*"],
  allow_headers = ["*"]
)

message = ""

@app.get("/orders")
def get_orders(param = None):
    global message
    buffer = message
    message=""
    if(param):
        return { "repo" : [o for o in repo if o.number == int(param)], "message": buffer}
    return {"repo" :repo, "message": buffer}

@app.post("/orders")
def create_order(dto : Annotated[Order, Form()]):
    repo.append(dto)

@app.post("/update")
def update_order(dto : Annotated[UpdateOrderDTO, Form()]):
    global message
    for o in repo:
        if o.number == dto.number:
            if dto.status != o.status and dto.status != "":
                o.status = dto.status
                message += f"Статус заявки №{o.number} изменен\n"
            if dto.description != "":
                o.description = dto.description
            if dto.master != "":
                o.master = dto.master
            return o
    return "Не найдено"