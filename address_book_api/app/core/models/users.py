from enum import unique
from typing import TypedDict

from sqlalchemy import Integer, Column, String, Table, DateTime

from app.db import metadata
from app.core.schemas.users import UserSchema


class UserDict(TypedDict):
    firstname: str
    lastname: str
    phone_number: int
    email: str
    address: str


userModel = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("firstname", String),
    Column("lastname", String),
    Column("phone_number", Integer, unique=True),
    Column("email", String, unique=True),
    Column("street", String),
    Column("city", String),
    Column("state", String),
    Column("zipcode", Integer),
)

# class UsersModel(UserSchema):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     firstname = Column(String, )
#     lastname = Column(String, )
#     phone_number = Column(Integer, )
#     email = Column(String, )
#     street = Column(String, )
#     city = Column(String, )
#     state = Column(String, )
#     zip_code = Column(Integer, )

#     def __init__(
#         self,
#         firstname: str,
#         lastname: str,
#         phone_number: int,
#         email: str,
#         street: str,
#         city: str,
#         state: str,
#         zip_code: int
#     ):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.phone_number = phone_number
#         self.email = email
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code

#     @property
#     def serialize(self) -> UserDict:
#         """
#         Return user in serializeable format
#         """
#         return {'id': self.id, 'firstname': self.firstname, 'lastname': self.lastname, 'phone_number': self.phone_number, 'email': self.email, 'address': f' {self.street} {self.city} {self.state} {self.zip_code}'}
