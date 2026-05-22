from database.connection import supabase


def register_user(email, password):

    try:

        response = supabase.auth.sign_up({
            "email": email,
            "password": password
        })

        return response.user

    except Exception as e:
        print(e)
        return None


def login_user(email, password):

    try:

        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        return response.user

    except Exception as e:
        print(e)
        return None