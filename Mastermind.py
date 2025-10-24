import random

print("Devinez le code de 4 chiffres (1 à 6)")
print("* = bonne position")
print("- = mauvais position")

secret_code = []
for i in range(4):
    secret_code.append(random.randint(1, 6))

attempts = 0
max_attempts = 10

while attempts < max_attempts:
    attempts = attempts + 1
    print(f"\nTentative {attempts}/{max_attempts}")
    
    user_input = input("Entrez 4 chiffres séparés par espace: ")
    input_list = user_input.split()
    
    if len(input_list) != 4:
        print("Il faut 4 chiffres!")
        attempts = attempts - 1
        continue
    
    player_guess = []
    has_error = False
    for x in input_list:
        try:
            number = int(x)
            if number < 1 or number > 6:
                print("Utilisez 1 à 6!")
                has_error = True
                break
            player_guess.append(number)
        except:
            print("Entrez des chiffres!")
            has_error = True
            break
    
    if has_error:
        attempts = attempts - 1
        continue
    
    correct_position = 0
    secret_temp = secret_code.copy()
    guess_temp = player_guess.copy()
    
    for i in range(4):
        if guess_temp[i] == secret_temp[i]:
            correct_position = correct_position + 1
            secret_temp[i] = -1
            guess_temp[i] = -2
    
    correct_number = 0
    for i in range(4):
        if guess_temp[i] != -2:
            for j in range(4):
                if guess_temp[i] == secret_temp[j]:
                    correct_number = correct_number + 1
                    secret_temp[j] = -1
                    break
    
    feedback = "*" * correct_position + "-" * correct_number
    if feedback == "":
        feedback = "Rien"
    print(f"Résultat: {feedback}")
    
    if correct_position == 4:
        print("\n GAGNÉ! 🎉")
        print(f"Code: {secret_code}")
        print(f"En {attempts} tentatives")
        break
else:
    print("\n PERDU!")
    print(f"Le code était: {secret_code}")