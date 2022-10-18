import math 

def func(x):
    return math.pow(x, 5) - ((10 * math.pow(x, 5))/9) + ((5 * x) / 21)

def secante(x_current, x_passed, error):
       
       
    while (x_current - x_passed) > error:
        print(f"Xn = {x_current}, Xn-1 = {x_passed}")
        x_future = x_current - (func(x_current) * ((x_current - x_passed) / (func(x_current) - x_passed)))
        print(f"Xn+1 = {x_future}")
        print(f"Error = {(x_current - x_passed)}")


        x_passed = x_current
        x_current = x_future


if __name__ == "__main__":
    secante(1, 0.8, 0.00001)