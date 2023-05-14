from graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    x1=10
    y1=10
    x2=100
    y2=100
    m = (y2-y1)/(x2-x1)
    c=y1-(m*x1)
    for x in range(x1,x2):
        y=(m*x)+c;
        aPoint = Point(x, y)
        aPoint.draw(win)
    win.getMouse() # pause for click in window
    win.close()
main()