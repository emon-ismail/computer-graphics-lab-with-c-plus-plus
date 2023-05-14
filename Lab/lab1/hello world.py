from graphics import *

# create a graphics window
win = GraphWin("Hello world", 400, 300)

# create the text object
text = Text(Point(200, 150), "Hello world")
text.setSize(36)
text.setTextColor("red")
text.setStyle("bold")

# draw the text on the window
text.draw(win)

# wait for the user to click the mouse
win.getMouse()

# close the window
win.close()
