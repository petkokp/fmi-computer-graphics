%int X1,Y1
%int color
%int xVal,yVal,RVal
M(X1,Y1+RVal)=color;
M(X1+RVal,Y1)=color;
try
    M(X1,Y1-RVal)=color;
    M(X1-RVal,Y1)=color;
catch
end
xVal=0;
yVal=RVal;
while xVal<yVal
    xVal=xVal+1;
    yVal=round(sqrt(RVal^2-xVal^2));
    eightSymmetric;
end
if (xVal==yVal)
    fourSymmetric;
end