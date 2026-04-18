import random 

# Variables
number = random.randint(1, 100)
num_try = 0 
tryed = "None"


print("Welcome to the game : The Right Price !")
print("The goal ? Try to guess the right price with less than a couples of tries. !")
identification = input("Identification ? : ")

if identification == "Bypass":
    print(number) 



while tryed != number:
    essaie = int(input("What is the right price ? : "))
    num_try += 1

    if tryed > number:
        print("Too big, retry !")

    elif tryed < number:
        print("Too small, retry !")

    elif tryed == number:
        print(f"Good job ! You've guessed the number in {num_try} tries")
