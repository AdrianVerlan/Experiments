import string
import secrets

def new_password(length):
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(i.islower() for i in password) and
            any(i.isupper() for i in password) and
            any(i.isdigit() for i in password)):
            return password

print("New Password:", new_password(5))
