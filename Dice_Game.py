#imports

import random
import time

player_score = 0
ai_score = 0

def dice():
    global player_score
    global ai_score
    player = random.randint(1,6)

    print("Player rolls: " + str(player))

    time.sleep(2)

    ai = random.randint(1,6)

    print("Computer rolls: " + str(ai))

    #time.sleep(2)

    if player > ai:
        print("You win!")
        player_score += 1
    elif player == ai:
        print("Tied game")    
    else:
        print("You lose!")
        ai_score += 1
    return player_score
    return ai_score

game_active = True


while game_active == True:
    print("Press enter to roll your dice.")
    roll = input()
    if roll == "N" or roll == "n":
        game_active = False
    else:
        dice()


print("You scored: " + str(player_score))
print("and the computer scored: " + str(ai_score))
if player_score > ai_score:
    print("You won, Congratulations!")
elif player_score == ai_score:
    print("You tied the match")
else:
    print("The computer won, better luck next time")    
