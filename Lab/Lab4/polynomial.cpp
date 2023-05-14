#include<iostream.h>
#include<graphics.h>
#include<conio.h>
#include<math.h>
void plot8pixel(int,int,int,int);
void main()
{
int x,y,r,h,k;
cout<<“\n\t\t\t\*Polynomial method to draw a circle*\n”;
cout<<“\nenter the x and y coordinates:-\n”;
cin>>h>>k;
cout<<“\nenter the radius:-\n”;
cin>>r;
x=0;
y=r;
int gd=DETECT,gm;
initgraph(&gd,&gm,””);
setbkcolor(WHITE);
while(x<=y)
{
plot8pixel(x,y,h,k);
x++;
y=sqrt((r*r)-(x*x));
}
setcolor(8);
outtextxy(115,70,”circle using polynomial method”);
getch();
closegraph();
}
void plot8pixel(int x,int y,int h,int k)
{
putpixel(x+h,y+k,8);
putpixel(x+h,-y+k,8);
putpixel(-x+h,y+k,8);
putpixel(-x+h,-y+k,8);
putpixel(y+h,x+k,8);
putpixel(y+h,-x+k,8);
putpixel(-y+h,x+k,8);
putpixel(-y+h,-x+k,8);
}