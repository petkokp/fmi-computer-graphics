%Време за изчисляване
MaxX=140;
MaxY=100;
M=zeros(MaxX,MaxY);
color=50;
timeStart=cputime;
for i=1:10000
    X1=1+floor(rand(1)*MaxX);
    X2=1+floor(rand(1)*MaxX);
    Y1=1+floor(rand(1)*MaxY);
    Y2=1+floor(rand(1)*MaxY);
    tema1_round;
    timeRounded=cputime-timeStart;
end
fprintf('Време за изчисляване по метода със закръгляне: %6.4f\n',timeRounded);
timeStart=cputime;
for i=1:10000
    X1=1+floor(rand(1)*MaxX);
    X2=1+floor(rand(1)*MaxX);
    Y1=1+floor(rand(1)*MaxY);
    Y2=1+floor(rand(1)*MaxY);
    tema1_bresenham;
    timeBresenham=cputime-timeStart;    
end
fprintf('Време за изчисляване по Брезенхам: %6.4f\n',timeBresenham);