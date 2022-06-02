#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sumsquares_1():
    sum = 0
    for a in range(1,101):
        x = a**2
        sum = sum + x
    return sum
    
def sumsquares_2():
    sum = 0
    for a in range(1,101):
        sum = a + sum 
    return sum**2


# In[ ]:


print(sumsquares_2() - sumsquares_1())

