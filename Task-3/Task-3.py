#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Calculate average of 5 numbers.

total = 0
for i in range(5):
    a = int(input("Enter the number"))
    total = total + a
print("Total",total)


# In[3]:


#2.Check whether number is even or odd.

num = int(input("Enter the number"))

if num%2==0:
    print("Number is even")
else:
    print("Number is odd")


# In[6]:


#3.Take a year and check whether it is leap year or not

year = int(input("Enter the year"))

if(year%4==0 and year%100!= 0 or year%400==0): 
    print("The year is a leap year") 
else:
    print("The year isn't a leap year")


# In[8]:


#4.Take a number and check whether it is zero, positive or negative.

a = int(input("Enter the number"))

if a<0:
    print("Thia number is negative")
elif a>0:
    print("This number is positive")
else:
    print("Given number is zero")


# In[9]:


#5.Take 2 numbers and display greatest number. (Also check equal number condition)

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

if a>b:
    print("Greter number :",a)
elif b>a:
    print("Greter number :",b)
else:
    print("Both numbers are equal")


# In[25]:


#6.Take a number and find factorial of that number.

num = int(input("Enter the number"))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   factorial=1
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[26]:


#7.Write a program to swap 2 numbers using third variable.

a = int(input("Enter the number"))
b = int(input("Enter the number"))

print("Given numbers a and b are:",a,b)

c=a
a=b
b=c

print("After sawapping numbers a and b are",a,b)


# In[27]:


#8.Take 2 numbers and find smallest number.

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

if a>b:
    print("smaller number :",b)
elif b>a:
    print("smaller number :",a)
else:
    print("Both numbers are equal")


# In[28]:


#9.Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

num = int(input("Enter the number"))

if num>100:
    print("Given number is greter than 100")
    
else:
    if num%2==0:
        print("Given number is less than 100 and even")
    else:
        print("Given number is less than zero and odd")


# In[29]:


#10.Take a number to print the square of a number if it is less than 10.

num = int(input("Enter the number"))

if num<100:
    print("Number is less than 100 and square of number is :",num*num)
else:
    print("Number is greter than 100")


# In[30]:


#11.Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")


# In[31]:


#12.Take 3 numbers and find greatest number using nested IF….ELSE statement.

# input three integer numbers 
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))

# conditions to find largest 
if a>b:
    if a>c:
        g=a
    else:
        g=c
else:
    if b>c:
        g=b
    else:
        g=c

# print the largest number 
print("Greater  = ",g)


# In[33]:


#13.Take 3 numbers and find smallest number using logical operator.



def smallest(x, y, z):
    c = 0
    
    while ( x and y and z ):
        x = x-1
        y = y-1
        z = z-1
        c = c + 1

    return c

x=int(input("Enter A: "))
y=int(input("Enter B: "))
z=int(input("Enter C: "))

print("Minimum of 3 numbers is",
    smallest(x, y, z))



# In[34]:


#14.Write a program to swap 2 numbers without taking third variable.

x=int(input("Enter x: "))
y=int(input("Enter y: "))

x = x + y
y = x - y
x = x - y
print("After Swapping: x =", x, " y =", y)


# In[35]:


#15.Take starting number and ending number from the user and print following series.

num = int(input("Enter stating number"))

while num>=0:
    print(num)
    print("  ")
    num=num-3


# In[ ]:




