import random
import os
from words import words

def hangman(words):
    word = random.choice(words)
    a = int(len(word))
    # print(word.upper())
    # print(f"{a} \n")
    i = 0
    ls = []
    l = []
    while i < a:
        ls.append("_")
        i+=1
    print(" ".join(ls))
    b = 0
    lives = 5
    while b  < a and lives > 0:
        
        
        guess = input("\n\nGuess a letter: ").lower()
        l.append(guess.upper())
        i = 0
        if guess in word:
            while i < a:
                if word[i] == guess:
                    ls.pop(i)
                    ls.insert(i,guess.upper())
                    b+=1
                i+=1
            print(" ".join(ls),end=" ")
            for i in range(1,lives + 1):
                if i == 1:
                    print("          \u2764\uFE0F", end="  ")
                else:
                    print("\u2764\uFE0F", end="  ")
            print("       Gussed Letters: "+" ".join(l))

        else:
            print("Wrong!")
            lives = lives - 1
            print(" ".join(ls),end=" ")

            for i in range(1,lives + 1):
                if i == 1:
                    print("          \u2764\uFE0F", end="  ")
                else:
                    print("\u2764\uFE0F", end="  ")
            print("       Gussed Letters: "+" ".join(l))
    if lives > 0:
        print("\nCongratulations!!!! You WON!")
    else:
        print("\nFuck off Loser!!!")
        print(f"The correct word is: {word}\n")
def lives(heart):
    for i in range(1,heart + 1):
        print("\u2764\uFE0F", end="  ")


print("\n\n\n********************Welcome to Hangman********************")
input("[Press Enter to continue]\n").lower()
a = "y"
while True:
    os.system('cls')
    if a == "y":
        hangman(words)
        a = input("Do you want to play again?\n(y/n)")
    elif a == "n":
        print("Fuck off!!!")
        exit()

