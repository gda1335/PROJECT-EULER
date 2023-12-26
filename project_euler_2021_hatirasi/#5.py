#https://projecteuler.net/problem=5

import math

import functools

def gcd(x,y):
    return math.gcd(x,y)



def lcm(x,y):
    return int(x*y/gcd(x,y))

#ebobx,y*ekokx,y=x*y


liste=range(1,21)

res=functools.reduce(lcm,liste)
#reduce liste ve fonksiyon alan (ekok fonk) ve bunu iterative olarak aliyor
print(res)