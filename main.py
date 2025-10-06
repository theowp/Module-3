# Question 1

# TODO: Create a string variable with a sentence
#sentence = "  Théo adore apprendre le Python avec ChatGPT.  "

# TODO: Convert the string to uppercase
#sentence_upper = sentence.upper()

# TODO: Convert the string to lowercase
#sentence_lower = sentence.lower()

# TODO: Capitalize the first letter of each word
#sentence_title = sentence.title()

# TODO: Replace a word in the string
#sentence_replaced = sentence.replace("Théo", "Zhour")

# TODO: Split the string into a list of words
#sentence_split = sentence.split()

# TODO: Join the list of words back into a string using a different separator
#sentence_joined = "-".join(sentence_split)

# TODO: Find the position of a specific word in the string
#position_python = sentence.find("Python")

# TODO: Check if the string starts with a specific word
#starts_with_theo = sentence.strip().startswith("Théo")

# TODO: Remove leading and trailing whitespace from a string
#sentence_stripped = sentence.strip()

# Print the results of each operation
#print("Original sentence:", sentence)
#print("Uppercase:", sentence_upper)
#print("Lowercase:", sentence_lower)
#print("Capitalized:", sentence_title)
#print("Replaced:", sentence_replaced)
#print("Split list:", sentence_split)
#print("Joined string:", sentence_joined)
#print("Position of 'Python':", position_python)
#print("Starts with 'Théo':", starts_with_theo)
#print("Stripped sentence:", sentence_stripped)

# Question 2 

#

# Question 3 

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for n in numbers:
    #print(n)
#for idx, val in enumerate(numbers, start=1):  # start=1 pour un index humain
    #print(f"index={idx}, value={val}")

#person = {"name": "Zhour", "age": 22, "height": 1.68}
#for key, value in person.items():
    #print(f"{key} -> {value}")
#for i in range(1, 11):
    #print(i)
#squares = [n*n for n in numbers]
# print(squares)

#table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
#print(table)

# Question 4
#a = 1  # on commence à 1
#while a <= 10:
 #   print(a)
  #  a = a + 1

# import random  # pour générer un nombre aléatoire

# # on choisit un nombre secret entre 1 et 10
# secret = random.randint(1, 10)

# # on initialise la variable du joueur
# guess = 0

# # tant que le joueur n’a pas trouvé, on continue
# while guess != secret:
#     guess = int(input("Devine un nombre entre 1 et 10 : "))

#     if guess < secret:
#         print("Trop petit !")
#     elif guess > secret:
#         print("Trop grand !")
#     else:
#         print("Bravo 🎉, tu as trouvé !")

# # Demande un nombre à l'utilisateur
# n = int(input("Entre un nombre : "))

# # Initialisation
# result = 1
# i = 1

# # Tant que i <= n, on multiplie result par i
# while i <= n:
#     result = result * i
#     i = i + 1

# # Résultat final
# print(f"La factorielle de {n} est {result}")

# Calculatrice simple avec une boucle while

while True:
    # Demander les nombres et l'opération
    num1 = float(input("Entre le premier nombre : "))
    op = input("Choisis une opération (+, -, *, /) : ")
    num2 = float(input("Entre le deuxième nombre : "))

    # Effectuer le calcul selon l'opération choisie
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("⛔ Erreur : division par zéro.")
            continue
    else:
        print("⛔ Opération invalide.")
        continue

    # Afficher le résultat
    print(f"Résultat : {result}")

    # Demander si on continue
    again = input("Voulez-vous continuer ? (o/n) : ")
    if again.lower() != "o":
        print("👋 Fin du programme.")
        break
