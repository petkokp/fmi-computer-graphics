%Çàäà÷à 2. Äà ñå íàïèøå ïðîãðàìà íà MATLAB, êîÿòî äà ðàñòåðèçèðà îêðúæíîñò 
%ïî ìåòîäà ñúñ çàêðúãëÿíå. 
%Äà ñå îðãàíèçèðà ãðàôè÷åí âõîä íà öåíòúðà è ðàäèóñà íà îêðúæíîñòòà.
MaxX=100;
MaxY=100;
M=zeros(MaxX,MaxY);
Ax=axes;
image(M');
set(Ax,'YDir','normal');
while (1)
    try
        [X,Y]=ginput(2);
    catch
        clear;
        clc;
        break;
    end
    X1=round(X(1));
    X2=round(X(2));
    Y1=round(Y(1));
    Y2=round(Y(2));
    dxVal=X2-X1;
    dyVal=Y2-Y1;
    RVal=round(sqrt(dxVal^2+dyVal^2));

    xVal=0;
    yVal=RVal;
    d=3-(2*RVal);

    color=50;
    M(X1,Y1)=color;
    M(X2,Y2)=color;

    circleBresenham;
    % circleRounded;

    pause(1);
    image(M');
    set(Ax,'YDir','normal');
    hold on;
end