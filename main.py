import random 

# Variable
number = random.randint(1, 100)
num_essaie = 0 
essaie = "None"


print("Bienvenue sur le jeu : Le Juste Prix")
print("Le but du jeu ? Essayez de deviner le nombre avec le moins d'essaie possible !")
identification = input("Identification ? : ")

if identification == "Bypass":
    print(number) 



while essaie != number:
    essaie = int(input("Quel est votre essaie ? : "))
    num_essaie += 1

    if essaie > number:
        print("Trop haut re-essaye")

    elif essaie < number:
        print("Trop bas re-essaye")

    elif essaie == number:
        print(f"Bravo ! Tu as obtenue le juste prix en {num_essaie} essaies")