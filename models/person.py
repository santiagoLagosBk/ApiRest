#python
from typing import Optional,List
#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class PersonBase(BaseModel):

    first_name : str = Field(
        ...,
        max_length = 18,
        min_length = 2,
        example = "santiago"
        
        )
    last_name : str = Field(
        ...,
        max_length = 18,
        min_length = 2,
        example = "Lagos"
        )

    birthday : Optional[str] 
    email: EmailStr = Field(...)
    description: Optional[str] = None
    topics : Optional[List] = None

    def to_dict(BaseModel):
        return vars(BaseModel)

class Person(PersonBase):
    password : str = Field(..., min_length=8)


class Person_out(PersonBase):
    pass