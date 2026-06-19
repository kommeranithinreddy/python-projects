users = [
    {"name": "Nithin", "is_admin": False},
    {"name": "Rahul", "is_admin": False},
    {"name": "Priya", "is_admin": True},
    {"name": "Kiran", "is_admin": False}
]


any(user['is_admin'] for user in users)

