from graphics import *
def main():
    win = GraphWin("My Circle", 1000, 1000)
    x1=100
    y1=100
    x2=100
    y2=200
    dx=x2-x1
    dy=y2-y1

    if abs(dx) > abs(dy):
        step=abs(dx)
    else:
        step=abs(dy)
   
    x_incr = dx / step;
    y_incr = dy / step;

    x=x1
    y=y1

    for nx in range(0,step):
        aPoint = Point(x, y)
        aPoint.draw(win)
        x= x+x_incr
        y=y+y_incr
   
    win.getMouse() # pause for click in window
    win.close()
main()