def multiply(x,y):
    if(y == 0):
        return 0
    if(y > 0):
        return(x + multiply(x, y - 1))

peopleTravelDaily = 1200000;
daysOfYear = 365;
peopleTravelYearly = multiply(peopleTravelDaily,daysOfYear);

print(peopleTravelYearly)