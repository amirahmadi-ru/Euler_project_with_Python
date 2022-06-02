#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# largest prime factor of the number 600851475143
def isprime(x):
    if x>1:
        for i in range(2,x):
            if x % i == 0:
                break
        else:
            return x
num = int(input("Please Enter : ")) 
largest = 0
for i in range(1,10000):
    if (num % i == 0) & (isprime(i)!= None):
        largest = i

print("largest prime factor of the number",num,"is",(largest))

