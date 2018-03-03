def power(base,exp):
    res = 1
    while exp >= 1:
        res *= base
        exp-=1
    return res

print(power(2,3))

def pow(base,exp):
    if exp == 1:
        return base
    else:
        return base * pow(base,exp-1);

print(pow(2,1))
