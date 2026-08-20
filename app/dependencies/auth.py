from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from app.database.supabase import supabase

security = HTTPBearer()


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):

    token = credentials.credentials

    try:

        user = supabase.auth.get_user(
            token
        )

        return user

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )