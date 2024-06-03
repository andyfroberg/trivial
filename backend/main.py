# Import necessary modules and classes
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

# FastAPI app instance
app = FastAPI()

# Database setup
engine = create_engine(os.environ.get("DATABASE_URL"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

# Database model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request data
class ItemCreate(BaseModel):
    name: str
    description: str

# Pydantic model for response data
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

# API endpoint to create an item
@app.post("/items/", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# API endpoint to read an item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

if __name__ == "__main__":
    import uvicorn
 
    uvicorn.run(app, host="127.0.0.1", port=8000)

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)


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
    # response = supabase.table('test_table').select("*").execute()
    # return {"response": response}
    return 


# @app.get("/sign_in")
# def sign_in_user_with_otp():
#     response = None
#     return {"response": response}

# @app.post("/sign_in")
# def sign_in_user_with_otp():
#     data = supabase.auth.sign_in_with_otp({
#         "email": 'example@email.com',
#         "options": {
#             "email_redirect_to": 'https://example.com/welcome'
#         }
#     })



# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}



#############################################
########### INGEST DATA #####################
#############################################

# post data to supabase table
@app.post("/v1/data")
def ingest_data():
    pass