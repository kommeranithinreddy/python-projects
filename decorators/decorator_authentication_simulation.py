def authenticate(function):
    def wrapper(value):
        if value.lower() == 'admin':
            function(value)
        else:
            print("Access Denied")
    return wrapper

@authenticate
def view_profile(role):
    print("Profile Opened")

@authenticate
def delete_user(role):
    print("User deleted")

view_profile('guest')
delete_user('admin')