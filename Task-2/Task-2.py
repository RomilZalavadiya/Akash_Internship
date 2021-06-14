#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello, World!") 

x = 5
y = "Romil"
print(x)
print(y)
print(type(x))
print(type(y))

thislist = ["apple", "banana", "cherry"]
print(thislist) 

print(thislist[1])

thislist[1] = "blackcurrant"
print(thislist)

thislist.append("orange")
print(thislist)

thislist.remove("apple")
print(thislist)

for x in thislist:
    print(x) 
    
thistuple = ("apple", "banana", "cherry") 
print(thistuple)

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict) 

a = 33 
b = 200
if b > a:
    print("b is greater than a") 
    
i = 1
while i < 6:
    print(i)
    i += 1
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# In[ ]:




