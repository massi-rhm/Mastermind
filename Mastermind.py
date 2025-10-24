import random

def generate_secret_code():
    code = []
    for _ in range(4):
        code.append(random.randint(1, 6))
    return code

secret_code = generate_secret_code()
print("code secret =", secret_code) 