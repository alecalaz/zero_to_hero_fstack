def try_login(email, password):
    if email == 'a@gmail.com' and password == '123':
        return True
    raise ValueError('These credentials are incorrect')
