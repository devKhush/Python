import turtle as trtl
from PIL import Image 

trtl.bgcolor('Black')
trtl.color('Red')
trtl.begin_fill()
trtl.pensize(3)
trtl.left(50)
trtl.forward(133)
trtl.circle(50,200)
trtl.right(140)
trtl.circle(50,200)
trtl.forward(133)
trtl.end_fill()

fileName = 'heart'

ts = trtl.getscreen()
ts.getcanvas().postscript(file=fileName + '.eps')
img = Image.open(fileName + '.eps') 
img.save(fileName + '.jpg')

print ("it is done")