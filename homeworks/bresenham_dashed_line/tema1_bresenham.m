%Ðñòåðèçèðàíå íà îòñå÷êà ïî ìåòîäà íà Áðåçåíõàì (tema1_bresenham)
%int X1,Y1,X2,Y2; parametri
%int x,y,dx,dy,incX,incY;
%int d, incUP, incDN, n, reverse;
dx=abs(X2-X1);
dy=abs(Y2-Y1);
reverse=(dx<dy);
if reverse
    d=X1;
    X1=Y1;
    Y1=d;
    d=X2;
    X2=Y2;
    Y2=d;
    d=dx;
    dx=dy;
    dy=d;
end
incUP=-2*dx+2*dy;
incDN=2*dy;
if (X1<=X2), incX=1; else incX=-1; end
if (Y1<=Y2), incY=1; else incY=-1; end
d=-dx+2*dy;
x=X1;y=Y1;n=dx+1;

dotsCounter=0;
draw=true;

while n
    if (draw)
        if (reverse)
            M(y,x)=color;
        else
            M(x,y)=color;
        end
    end
    x=x+incX;
    if (d>0)
        y=y+incY;
        d=d+incUP;
    else
        d=d+incDN;
    end

    dotsCounter = dotsCounter + 1;

    if draw
        if dotsCounter >= visible
            dotsCounter = 0;
            draw = false;
        end
    else
        if dotsCounter >= invisible
            dotsCounter = 0;
            draw = true;
        end
    end

    n=n-1;
end