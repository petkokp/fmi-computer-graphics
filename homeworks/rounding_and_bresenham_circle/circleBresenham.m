% circleBresenham
while xVal <= yVal
    if d < 0
        d = d + (4 * xVal)+6;
    else
        d = d + (4 * (xVal-yVal)) + 10;
        yVal = yVal - 1;
    end
    xVal = xVal + 1;
    eightSymmetric;
end