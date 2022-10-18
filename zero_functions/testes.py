import math

def calculo(x):
    f1 = math.pow(x, 5) - ((10 * math.pow(x, 5))/9) + ((5 * x) / 21)
    f2 = (5 * math.pow(x, 4)) - ((50 * math.pow(x, 4)) / 9) + (5 / 21)
    result = x - (f1/f2)
    error = (x - result)
    print(f"fX = {f1}, fX' = {f2}, result = {result}, error = {error}")
    return result, error

def calculo2(x):
    result = math.pow(x, 5) - ((10 * math.pow(x, 5))/9) + ((5 * x) / 21)
    print(result)

def newton_raphson(x == 0, error == 0.01, ):
    while error > 0.0001:
        x, error = calculo(x)

if __name__ == "__main__":
    
    # calculo2(0.1)