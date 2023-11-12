% int X1,Y1,xVal,yVal
% int color
M(X1+xVal,Y1+yVal)=color;
M(X1+yVal,Y1+xVal)=color;
try
    M(X1-xVal,Y1-yVal)=color;
    M(X1-xVal,Y1+yVal)=color;
    M(X1+xVal,Y1-yVal)=color;
    M(X1-yVal,Y1-xVal)=color;
    M(X1-yVal,Y1+xVal)=color;
    M(X1+yVal,Y1-xVal)=color;
catch
end