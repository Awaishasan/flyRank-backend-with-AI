from pydantic import BaseModel, EmailStr, Field

class SignUpRequest(BaseModel):
    email : EmailStr
    password: str = Field(
        min_length=8
    )

class LoginRequest(BaseModel):
        email :EmailStr
        password: str=Field(
            min_length=8
        )
class TokenResponse(BaseModel):
      access_Token: str
      refresh_Token:str




