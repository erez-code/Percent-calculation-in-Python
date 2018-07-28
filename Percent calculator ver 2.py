
# coding: utf-8

# In[ ]:


def percent2(a,b):
    return a*100/b
a =int(input("This program can tell what PERCENT of the WHOLE number your PART represents! First, please type your PART: "))
b =float(input("Now, please type the WHOLE number: "))
print("The result is:", int(percent2(a,b)),"%")

delay = input("Press enter to finish")
