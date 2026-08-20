from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.auth import (
    verify_token
)

router = APIRouter(
    prefix="/protected",
    tags=["Protected"]
)


@router.get("/profile")
def profile(
    user=Depends(verify_token)
):

    return {
        "message":
        "Welcome to your profile",

        "user":
        user.user.email
    }