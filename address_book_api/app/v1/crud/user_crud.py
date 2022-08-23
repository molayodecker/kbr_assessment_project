import json
import re

from fastapi import HTTPException

from app.core.schemas.users import UserSchema
from app.core.models.users import userModel
from app.db import database


def check_email_valid(email):
    """Check if a email ( string ) is in valid format
    :param email:
    :return: True if valid, False if invalid
    """

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True


async def email_exist(email: str):
    query = query = f"SELECT * FROM users WHERE email = '{email}'"
    return await database.fetch_one(query=query)


async def phone_number_exist(phone: str):
    query = query = f"SELECT * FROM users WHERE phone_number = '{phone}'"
    return await database.fetch_one(query=query)


async def post(payload: UserSchema):
    """
    Creates new user address book
    :param: 
    :return: {message: success}
    """

    data = payload.json()
    json_dict = json.loads(data)
    email = json_dict.get('email', None)
    is_email_valid = check_email_valid(email)
    if not is_email_valid:
        raise HTTPException(status_code=406, detail="Email is incorrect")
    phone = json_dict.get('phone_number', None)
    email_resp = await email_exist(email)
    phone_resp = await phone_number_exist(phone)
    if email_resp:
        raise HTTPException(status_code=409, detail="Email already exist")
    if phone_resp:
        raise HTTPException(
            status_code=409, detail="Phone number already exist")
    query = userModel.insert().values(**json_dict)
    return await database.execute(query=query)


async def get_all():
    query = "SELECT firstname, lastname, phone_number, email, street || ' ' || city || ' ' || state || ' ' || zipcode AS address FROM users"
    result = await database.fetch_all(query=query)
    return result


async def search(term: str):
    query = f"SELECT * FROM users WHERE (firstname LIKE '%{term}%' OR lastname LIKE '%{term}%') ORDER  BY lastname"
    result = await database.fetch_all(query=query)
    return result
