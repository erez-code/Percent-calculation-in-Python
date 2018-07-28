
# coding: utf-8

# In[ ]:


def percent(a,b):
    return b*a /100
a =int(input("This program can tell what PART of the WHOLE number a PERCENT represents! First, please type the WHOLE number: "))
b =float(input("Now, please type the PERCENT: "))
print("The result is:", int(percent(a,b)))

delay = input("Press enter to finish")
