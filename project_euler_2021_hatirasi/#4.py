"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def checkpal(x):
    strn=str(x)
    rev=strn[::-1] #Ters 
    if strn==rev:
        return True
    else:
        return False
    
bigpal=0

"""
3 bas sayilarin carpımıyla elde edilcek en buyuk palindrom
"""
    
for i in range(100,1000):
    for j in range(100,1000):
        if checkpal(i*j) and i*j >bigpal:
            bigpal=i*j

print(bigpal)
    

#%%
result=[]
for number1 in range(100,1000):
    for number2 in range(100,1000):
        a=(number1*number2)
        b=str(a)
        if (b==b[::-1]): #check pal 
            result.append(a)
print(max(result))