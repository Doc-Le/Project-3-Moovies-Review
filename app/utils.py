from .models import (
    User,
)

"""
Get user object from session
"""
def get_user_session():
    return User(username ="guest", password="", authenticated=False)

"""
Clear user session and set guest user object
"""
def clear_user_session():
    # clear user session
    # set guest user
    user = get_user_session()
    return user