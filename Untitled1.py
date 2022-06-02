#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Coefficient3or5():
    lst = []
    sum_i = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            lst.append(i)
            sum_i = sum_i + i
#             print(i, True)
    print("The sum is", sum_i)
#     print(lst)
Coefficient3or5()

