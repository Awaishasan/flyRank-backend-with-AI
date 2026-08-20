from fastapi import APIRouter, Depends, Response

from app.dependencies.auth_dependency import get_current_user
from app.database.supabase import supabase

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


@router.post("/logout")
def logout(current_user=Depends(get_current_user)):
    supabase.auth.sign_out()
    return Response(status_code=204)