import random

def roll(): # this function will always be called to roll the dice
    dice = random.randint(1,6)
    return dice

while True:
    players = input("Enter the number of players (2-4) : ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4 :
            break
        else:
            print("Must be between 2-4 players")
    else:
        print("Invalid, Try Again")

max_score = 50
player_scores = [] # storing all scores for the players
player_scores = [0 for i in range(players)] # this can give us a list that makes a list for all players and puts 0 - list comprehension