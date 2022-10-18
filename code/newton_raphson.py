import math


def f_x(x, y):
    return math.pow(x, 3) * math.cos(x), math.pow(y, 3) * math.cos(y)

def f_linhax(x, cx):
    return x - (math.pow(x, 3) * math.cos(x) / cx) 

def newton_raphson(x):
    print(f_x(x))
    print(f_linhax(x))
    current_x = x - (f_x(x)/f_linhax(x) )
    print(current_x)
    print(f"Tolerance: {x - current_x}")  


if __name__ == '__main__':
    newton_raphson(0.33466)