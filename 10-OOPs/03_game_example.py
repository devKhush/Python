class Remote():
    pass


class Player:
    def moveRight(self):
        pass

    def moveLeft(self):
        print('Player moves Left')

    def moveTop(self):
        pass

    def moveBottom(self):
        print('Player moves Bottom')


remote1 = Remote()
player1 = Player()

player1.moveLeft()
player1.moveBottom()

if (remote1.isLeftPressed()):
    player1.moveLeft()
