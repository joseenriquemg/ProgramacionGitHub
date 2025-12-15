def user_schema(user) -> dict:
    # El id en base de datos es _id
    return {"id": str(user["_id"]),
    "username": user["username"],
    "fullname": user["fullname"],
    "email": user["email"],
    "disabled": bool(user["disabled"]),
    "password": user["password"]}

def users_schema(users) -> list:
    return [user_schema(user) for  user in users]