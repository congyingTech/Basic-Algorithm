import numpy as numpy


def hello():
    print("This is my first time use vs code for python")

def swap(a, b):
    t = a
    a = b
    b = t
    return a, b

if __name__ == "__main__":
    hello()
    a = 10
    b = 11
    a, b = swap(a, b)
    print(a, b)