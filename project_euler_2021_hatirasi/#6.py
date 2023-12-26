karetop=0
for i in range(101):
    karetop=karetop+i**2
print(karetop)
    
top=0
for i in range(101):
    top+=i
    top=top**2
print(top)


print(top-karetop)

#%%
#Wiser

sum_of_sq=0
sq_ofs=0

sum=0

for i in range(101):
    sum+=i
    sum_of_sq+=i*i
    
    
a=sum*sum-sum_of_sq

print(a)