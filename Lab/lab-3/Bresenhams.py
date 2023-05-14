from graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    x1=100
    y1=100
    x2=300
    y2=200
    dx=x2-x1
    dy=y2-y1
    x=x1
    y=y1
    dt= 2*(dy-dx)
    ds=2*dy
    d=(2*dy)-dx
    aPoint = Point(x, y)
    aPoint.draw(win)
    for x in range(x+1,x2):
        if d<0:
            d=d+ds
        else:
            y=y+1
            d=d+dt
        bPoint = Point(x, y)
        bPoint.draw(win)

    win.getMouse() # pause for click in window
    win.close()
main()
