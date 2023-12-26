"""

https://projecteuler.net/problem=3

the largest prime factor ?
"""


import math 

def primeB(a):
    is_pr=True
    
    for i in range(2,int(math.sqrt(a))+1):
        #kendinden kucuk olan tum sayilara bakmak zorunda degiliz!
        #karekokune kadar olan sayilar denenicek'
        if a%i==0:
            is_pr=False
            continue
    return is_pr

num= 600851475143

biggest=1

for i in range (2,int(math.sqrt(num))):
    if num %i==0 and primeB(i):
        biggest=i
print(biggest)
        