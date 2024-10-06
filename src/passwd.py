import secrets
import string


def generate_strong_password(length=8):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password


password = generate_strong_password(10)
print(f"Foi gerado uma senha forte para o usuário: {password}")