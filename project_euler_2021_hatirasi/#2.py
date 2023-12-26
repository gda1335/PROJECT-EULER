#https://projecteuler.net/problem=2

#Even fibonacci 4x10^6 dan kucuk fib sayilari 
#listeler

fib=list()

fib.append(1)
fib.append(2)
i=2

while True:
    if fib[i-1]+fib[i-2]<4000000:
        fib.append(fib[i-1]+fib[i-2])
        i+=1
    else:
        break
s=0  
for i in fib:
    if i%2==0:
        s+=i
print(s)
print(len(fib)) 


#alternative and wiser!
#%%
so=2
a=1
b=2
while True:
    c=a+b
    a=b
    b=c
    
    if c%2==0:
        so+=c
    if c>4000000:
        break
print(so)

#%%

sumi=2
a=1
b=2
while True:
    c=a+b
    a,b=b,c #same code but difference here !

    if c%2==0:
        sumi+=c
    if c>4000000:
        break
print(so)
    
    
        
