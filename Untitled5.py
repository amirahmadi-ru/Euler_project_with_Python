#!/usr/bin/env python
# coding: utf-8

# In[14]:


x=2
lst = []
while (x<=40000):
    status = True
    for i in range(2,x//2):
        if x % i == 0:
            status = False
    if status == True:
#         print(x, "It's prime")
        lst.append(x)
#     else:
#         print(x, "It's not prime")
    x = x+1
print(lst)


# In[21]:


print(lst[5000])

