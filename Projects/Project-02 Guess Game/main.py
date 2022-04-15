import random


class GuessGame:

    def __init__(self, lowLimit, highLimit) -> None:
        self.lowLimit = lowLimit
        self.highLimit = highLimit

    def greet(self) -> None:
        print('Hello, user!\n')

    def getRandomNumber(self) -> int:
        return random.randint(self.lowLimit, self.highLimit)

    def sayBye(self):
        print('\nThanks for Playing! \n:)')

    def readPreviousHighScore(self) -> int:
        with open('HighScore.txt') as file:
            highScore = file.read().strip()
        if highScore != '':
            return int(highScore)

    def showScore(self, prevHighScore, currScore) -> None:
        if prevHighScore == None or prevHighScore > currScore:
            print('You have just broken High score!!!')
            print(f'Previous High Score: {prevHighScore}')
            print(f'Current Score: {currScore}')

            with open('HighScore.txt', 'w') as file:
                file.write(str(currScore))
        else:
            print(f'Previous High Score: {prevHighScore}')
            print(f'Current Score: {currScore}')

    def play(self) -> None:
        self.greet()
        randomGuess = self.getRandomNumber()
        userGuess = None
        numOfGuess = 0

        while (userGuess != randomGuess):
            numOfGuess += 1
            userGuess = int(input('Guess a Number: '))
            if userGuess > randomGuess:
                print('Lower Number Please!\n')
            elif randomGuess > userGuess:
                print('Higher Number Please!\n')
            else:
                print('Correct!!!')
                print(
                    f'You correctly guessed the number in {numOfGuess} times\n')

        prevHighScore = self.readPreviousHighScore()
        self.showScore(prevHighScore, numOfGuess)
        self.sayBye()


game = GuessGame(1, 100)
game.play()
