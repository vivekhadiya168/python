# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
import random

def game():
    print("you are playing the game...")
    score =  random.randint(1, 62)
    # fetch the highscore
    with open("chapter_09_ps/hi_score.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0
    print(f"your score : {score}")
    if(score>highscore):
        # write this highscore to the file
        with open("chapter_09_ps/hi_score.txt", "w") as f:
            f.write(str(score))

    return score

game()

