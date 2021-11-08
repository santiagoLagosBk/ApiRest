
from pydantic import BaseModel
from pydantic import Field


class LoginOut(BaseModel):
    username: str = Field(...,
    min_length = 8,
    max_length = 21,
    example = "santiax"
    )
    message: str = Field(default = "Login succesfully")


class Login(LoginOut):

    password: str = Field(...,
    min_length = 8,
    example = "contrasena12345"
    )
    


