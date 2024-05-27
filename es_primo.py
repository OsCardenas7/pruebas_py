def esPrimo(n):
    for x in range(2, (n//2)+1):
        if n%x == 0:
            return False
    return True

n = 140
p = 2
while n != 1:
    while not esPrimo(p):
        p = p + 1
    if n % p == 0:
        n = n // p
        print(p)
    else:
        p = p + 1
