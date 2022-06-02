#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
def even_num(x):
    if x % 2 == 0:
        return True
    else:
        return False
one = 1
two = 2
sum = 0
while (one < 4*10**6):
    print("My first number is :", one)
    if even_num(one):
        print("It's a even number")
        sum = sum + one
        print("-------------> My sum is : ", sum)
    new = one + two
    one = two
    two = new
print(sum)

