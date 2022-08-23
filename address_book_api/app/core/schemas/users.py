from pydantic import BaseModel
from typing import Optional

from sqlalchemy import func

from sqlalchemy.ext.hybrid import hybrid_property


class UserSchema(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    phone_number: Optional[int]
    email: Optional[str]
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zipcode: Optional[int]

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "firstname": "Jules",
                "lastname": "Kroll",
                "phone_number": 2127020707,
                "email": "string",
                "street": "805 3rd Ave 29th floor",
                "city": "New York",
                "state": "NY",
                "zipcode": 10022
            }
        }


class UserDB(UserSchema):
    id: int
