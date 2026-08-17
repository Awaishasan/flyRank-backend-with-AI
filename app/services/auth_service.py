from fastapi import HTTPException

from app.repositories.auth_repository import (
    create_user,
    login_user
)


def signup_service(email, password):

    response = create_user(
        email,
        password
    )

    if not response.user:

        raise HTTPException(
            status_code=400,
            detail="Signup failed"
        )

    return {
        "message": "User created successfully"
    }


def login_service(email, password):

    response = login_user(
        email,
        password
    )

    return {
        "access_token":
        response.session.access_token,

        "refresh_token":
        response.session.refresh_token
    }