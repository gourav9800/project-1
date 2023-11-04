#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create a Python program that asks the user for a month (1-12) and then prints the corresponding 
#season ("Spring," "Summer," "Fall," or "Winter").

month=input("type any month")

if month in ('jan','feb','march'):
    print("spring")
elif month in ("april","may","june"):
    print("summer")
elif month in("jully","aug","sep"):
    print("fall")
else:
    print("winter")


# In[ ]:


#Write a Python program that takes two numbers as input and prints the larger number.

a=input("please enter any no.")
b=input("please enter any no.")
c=max(a,b)
print (c)


# In[ ]:


#Write a Python program that determines whether a given year is a leap year or not. Use the leap year rules mentioned earlier.

year=int(input("please enter the year:"))
if (year%4==0 and year%100!=0) or (year%400==0):  
    print("this is a leap year")
else:
    print("this is not a leap year")


# In[ ]:


#Create a program that takes an integer as input and checks if it's positive, negative, or zero. Print an appropriate message.

number=int(input("please enter any no.:"))
if number>0:
    print("this value is positive")
elif number==0:
    print("this value is zero")
else:
    print("this value is negitive")


# In[ ]:


#Write a Python program that asks the user for their age and gender.
#Based on their age and gender, print a message like "You are a young man" or "You are an old woman."



age = int(input("Please enter your age: "))
gender = input("Please select gender (M/F): ")

if age >= 60:
    if gender == "M":
        print("You are an old man")
    elif gender == "F":
        print("You are an old woman")
else:
    if gender == "M":
        print("You are a young man")
    elif gender == "F":
        print("You are a young woman")


# In[ ]:


#Create a program that takes a temperature in Celsius and converts it to Fahrenheit. 
#Display the result with an appropriate message.

c=float(input("enter the tem in celcious:"))
F=(c*(9/5))+32
print("tem in fel is:",F)


# In[ ]:


#Write a Python program that calculates the shipping cost based on the weight of a package. Use the following rules:
#- Weight <= 2 pounds: $5.00
#- 2 pounds < Weight <= 10 pounds: $10.00
#- Weight > 10 pounds: $15.00

Weights=int(input("enter the weight in pound:"))
if Weights <= 2:
    print("shipping cost is $5.00")
elif Weights <= 10:
    print("shipping cost is $10.00")
elif  Weights > 10:
    print("shipping cost is $15.00")
else:
    ("invalid")


# In[ ]:


#Write a Python program that checks if a given year is a "century year" (ends in 00). If it's a century year, check if it's a leap year.

year=int(input("mention year"))

if year%400==0 and year%100==0 :
    print("centuary year and leap year ")
elif year%4==0 and year%100!=0:
    print("leap year")
elif year%100==0:
    print("centuary year")
else:
    print('invalid')


# In[ ]:


#Create a program that asks the user for three numbers and then prints them in ascending order.


no1=int(input("enter1:"))
no2=int(input("enter2:"))
no3=int(input("enter3:"))

number=[no1,no2,no3]
number.sort()
print(number)


# In[ ]:


#Create a program that asks the user for a number and then determines if it's even or odd. Print an appropriate message.


number=int(input("enter any no.:"))

if number%2==0:
    print("this no. is even")

else:
    print("this no. is odd no")


# In[ ]:




