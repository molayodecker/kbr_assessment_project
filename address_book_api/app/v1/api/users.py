from typing import List, Dict

from fastapi import APIRouter, status
from app.core.schemas.users import UserSchema, UserDB

from app.v1.crud import user_crud

router = APIRouter()


@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_new_user(payload: UserSchema):
    user_id = await user_crud.post(payload)

    if user_id:
        return {'message': 'successful'}


@router.get("/users")
async def get_all_users():
    return await user_crud.get_all()


@router.get("/users/{term}")
async def search(term: str):
    if term:
        return await user_crud.search(term=term)
    else:
        return await user_crud.get_all()
