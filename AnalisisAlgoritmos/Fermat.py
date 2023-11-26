import random

def power(x, y, p):
    result = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            result = (result * x) % p
        y = y >> 1
        x = (x * x) % p
    return result

def fermat_test(n, k):
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Usar la función:
n = 561  # un número de Carmichael
k = 5    # número de iteraciones
print(fermat_test(n, k))  # Output: True Tenemos que entender que esto es un algoritmo tipo las vegas
