# Crie um programa que faça o computador jogar jokenpo com você

from random import randint
from time import sleep

options = ("ROCK","PAPER","SCISSOR")
cpu = randint(0,2)

print("="*20)
print("Welcome to the AMAZING ROCK, PAPER, SCISSOR GAME")
sleep(1)
print("Are you ready?")
sleep(1)
print("Let's go...")
sleep(1)
print("-"*20)
print("[0] - ROCK")
print("[1] - PAPER")
print("[2] - SCISSOR")

player = int(input("Choose an option above: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-=-"*15)
print(f"You choose {(options[player])}")
print(f"I choose {(options[cpu])}")

if (cpu != player):
    if (cpu == 0):
        if (player == 1):
            print ("You won!")
        elif (player == 2):
            print ("I win!")
    elif (cpu == 1):
        if (player == 0):
            print ("I win!")
        elif (player == 2):
            print ("You won!")
    elif (cpu == 2):
        if (player == 0):
            print ("You won!")
        elif (player == 1):
            print ("I win!")
elif(cpu == player):
    print("It's a Draw!")
print("-=-"*15)
