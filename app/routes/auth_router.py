# from fastapi import APIRouter,HTTPException,status
# from dotenv import load_dotenv
# from app.schemas.auth_schema import LoginRequest, SignUpRequest
# import os




# load_dotenv()

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# router = APIRouter(
#     routes="/auth",
#     tags=["Authentication"]
# )


# @router.post("/signup")
# def signup():
#      return {
#         "message": "Signup successful"
#     }

# @router.post("/login")
# def login():
#      return {
#         "message": "login successful"
#     }

from fastapi import APIRouter

from app.schemas.auth_schema import (
    SignUpRequest,
    LoginRequest
)

from app.services.auth_service import (
    signup_service,
    login_service
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
async def signup(data: SignUpRequest):

    return signup_service(
        data.email,
        data.password
    )


@router.post("/login")
async def login(data: LoginRequest):

    return login_service(
        data.email,
        data.password
    )