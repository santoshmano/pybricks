def  pow(dblbase, ipower):
    if ipower == 1:
        return (dblbase)
    elif ipower == 0:
        return float(1)
    elif ipower == -1:
        return (1/dblbase)
    else:
        if ipower > 0:
            return (1*dblbase)*(pow(dblbase, ipower-1))
        elif ipower < 0:
            return round((1/dblbase)*(pow(dblbase, ipower+1)), 9)


print(pow(10, 3))
print(pow (4.5, -3))
print(pow (9, 0))
