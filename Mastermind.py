import random

def generate_secret_code():
    code = []
    for _ in range(4):
        code.append(random.randint(1, 6))
    return code

secret_code = generate_secret_code()

def get_player_guess():
    while True:
        guess_input = input("Entrez 4 chiffres (1-6) séparés par des espaces : ")
        guess_str = guess_input.split()
        if len(guess_str) != 4:
            print("Il faut exactement 4 chiffres !")
            continue
        try:
            guess = [int(x) for x in guess_str]
        except:
            print("Entrez uniquement des chiffres !")
            continue
        if any(x < 1 or x > 6 for x in guess):
            print(" Chaque chiffre doit être entre 1 et 6 !")
            continue
        return guess
    