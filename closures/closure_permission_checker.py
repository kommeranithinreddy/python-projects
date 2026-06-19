def outer(role):
    def admin_role(request):
        print(f'{request} for {role} permission granted')
    def guest_role(request):
        print(f'{request} for {role} permission denied')

    if role == 'admin':
        return admin_role
    if role == 'guest':
        return guest_role

admin = outer('admin')
guest = outer('guest')

admin('delete')
guest('delete')
