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
player_scores = [0 for i in range(players)] # this can give us a list that makes a list for all players and puts 0 - list comprehension

while max(player_scores) < max_score:

    for player_idx in range(players):
        print("\nPlayer ",player_idx+1," turn has started\n")
        current_score = player_scores[player_idx]

        while True:

            should_roll = input("Would you like to roll (Y) : ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled a 1, Turn Done!")
                break
            else:
                current_score += value
                print("You rolled a: ",value)
            
            print("current score = ",current_score)
        player_scores[player_idx] = current_score
        print("Your total score is = ",player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number ",winning_idx+1," is the winner!")
