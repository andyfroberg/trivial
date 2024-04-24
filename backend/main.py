from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv


import os
from supabase import create_client, Client

load_dotenv()

app = FastAPI()


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None




# class User(BaseModel):
#     id: int
#     name: str
#     email: str

# class Round(BaseModel):
#     id: int
#     questions: list[Questions]


# class UserPreferences(BaseModel):
#     ...

# class Question(BaseModel):
#     id: int
#     category: str
#     difficulty: int
#     text: str
#     correct_answer: Answer.id

# class Answer(BaseModel):
#     id: int
#     text: str
#     question: list[Question.id]

# class TriviaQuestion(BaseModel):
#     id: int
#     user: User
#     answered_correctly: bool




@app.get("/")
def read_root():
    response = supabase.table('test_table').select("*").execute()
    return {"response": response}

@app.get("/signiup")
def read_signup():
    pass

@app.post("/signup")
def create_user():
    res = supabase.auth.sign_up(
        email= "",
        password= "",
    )



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

