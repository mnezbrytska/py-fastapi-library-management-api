from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
#
# import crud
# import schemas
# from db.engine import SessionLocal
# from db.models import PackagingType

app = FastAPI()

#
# def get_db() -> Session:
#     db = SessionLocal()
#
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

#
# @app.get("/cheese_types/", response_model=list[schemas.CheeseType])
# def read_cheese_types(db: Session = Depends(get_db)):
#     return crud.get_all_cheese_types(db=db)