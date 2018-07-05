from user import User

users = [
    User(1, 'Bob', 'asdf')
]

username_mapping = { u.username: u for u in users }
userid_mapping = { u.id: u for u in users}

# Given a username/password we'll authenticate
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

#
# This will map the users by username and userid, that is you can obtain directly by users['bob'] or users[1] 
# #