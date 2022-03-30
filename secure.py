import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
#Security Part of the project, includes encryption and hashing functions that derive the encryption key from the password
def PSHs(x):
    y = x.encode('utf-8')
    salt = b'PUT YOUR SALT HERE' #16 char salt between the ' '
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256, length=32, salt=salt, iterations=100000
    )
    return base64.urlsafe_b64encode(kdf.derive(y))

def fencrypt(x):
    f = Fernet(x)
    with open("Encrypt.txt", "rb") as file:
        file_data = file.read()
    f_enc = f.encrypt(file_data)
    with open("Encrypt.txt", "wb") as file:
        file.write(f_enc)

def fdecrypt(x):
    f = Fernet(x)
    with open("Encrypt.txt", "rb") as file:
        f_enc = file.read()
    f_dec = f.decrypt(f_enc)
    with open("Encrypt.txt", "wb") as file:
        file.write(f_dec)