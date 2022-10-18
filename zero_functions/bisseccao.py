import math
import random

def func(x):
    return math.pow(x, 5) - ((10 * math.pow(x, 5))/9) + ((5 * x) / 21)
    

def bisseccao(a = 0, b = 0, error = 0.001):
    k = 1
    m = func(a)
    
    while True:
        print(f"k = {k}")
        print(f"(b - a) = {(b - a)}")
        if (b - a) < error:
            result = random.uniform(a, b)
            print(f"Result = {result}")
            break
        x = (a + b) / 2
        print(f"x = {x}")
        print(f"(m * func) = {(m * func(x))}")
        if (m * func(x) > 0): 
            a = x
            print(f"a = {a}")
            k += 1
            print("\n")
            continue
        b = x
        print(f"b = {b}")
        
        k += 1
        print("\n")
        


if __name__ == "__main__":
    bisseccao(-0.75, -0.25, 0.0001)