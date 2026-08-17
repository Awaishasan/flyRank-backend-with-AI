from app.database.supabase import supabase


def create_user(email, password):

    return supabase.auth.sign_up(
        {
            "email": email,
            "password": password
        }
    )


def login_user(email, password):

    return supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )