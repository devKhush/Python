import random as rand


def getGameScore():
    score = rand.randint(1000, 2000)
    return score


with open('09_06_pr_02_high_score.txt') as file:
    # prev_high_score = file.readline().strip()  # both works
    # not converting to int now, coz file might be blank also
    prev_high_score = file.read().strip()

curr_score = getGameScore()

if prev_high_score == '' or curr_score > int(prev_high_score):
    print('Your high score: ', curr_score)
    print('Previous High Score: ', ("'NA'"
          if prev_high_score == '' else int(prev_high_score)))

    with open('09_06_pr_02_high_score.txt', 'w') as file:
        file.write("  "+str(curr_score)+"   \n")
        print('High score Updated')

else:
    print('Your high score: ', curr_score)
    print('Previous High Score: ', prev_high_score)
    print('High score Not Updated')
