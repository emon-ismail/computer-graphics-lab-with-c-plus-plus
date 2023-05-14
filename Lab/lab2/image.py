from graphics import *

# create a graphics window
win = GraphWin("Image", 400, 300)

# create the Image object
img = Image(Point(200, 150), "example.png")

# draw the image on the window
img.draw(win)

# wait for the user to click the mouse
win.getMouse()

# close the window
win.close()
