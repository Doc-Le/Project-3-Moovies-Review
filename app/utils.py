from flask import session


"""
Set user object from session
"""
def set_user_session(username, authenticated):
    session['user'] = {
        "username": username,
        "authenticated": authenticated
    }

"""
Get user object from session
"""
def get_user_session():
    if 'user' in session:
        return session['user']
    else:
        set_user_session(username="guest", authenticated=False)
        return session['user']

"""
Is authenticated
"""
def is_authenticated():
    user = get_user_session()
    return bool(user['authenticated'] == False)

"""
Clear user session and set guest user object
"""
def clear_user_session():
    session.pop('user', None)
