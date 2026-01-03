# print("hello world","this is the first program") 
# print("my age is 27")
# print("my name is manoj")
# print(23+25)
# name = "manoj"
# age = 25
# address = "lalpur"
# price = 25.55
# print(name,age,address)
# print("my name is:",name)
# -----------------------------------
# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# sum = a + b
# print("the sum of two number is:", sum)
# ----------------------------------------
# a = int(input("enter length of one side os square:"))
# print("The are of Square is :", a**22)
# -------------------------------
# first = float(input("enter first num:"))
# second = float(input("enter second num:"))
# print("the average of both is",(first+second)/2)
# -------------------------------
# first = int(input("enter first number:"))
# second = int(input("enter second nunber:"))
# print(first>=second)
# -----------------------------
# f_name = input("enter your first name:")
# print("welcome",f_name,len(f_name))
# print(f_name.find("$"))
# --------------------------------
# conditional statement 
# light = "green".lower()
# if (light == "red"):
#     print("Stop")
# elif(light == "yellow"):
#     print("Look")
# elif(light == "green"):
#     print("Go")
# else:
#     print("Light is broken")
# print("End of code")

# ------------------------------
# marks = int(input("Enter students marks:"))
# if(marks >= 90):
#     print("Your Grade is A+")
# elif(marks >=80 and marks <90):
#     print("Your Grade is A")
# elif(marks >=70 and marks <80):
#     print("Your Grade is B+")
# elif(marks >=60 and marks <70):
#     print("Your Grade is B")
# elif(marks >=50 and marks <60):
#     print("Your Grade is C+")
# elif(marks >=40 and marks <50):
#     print("Your Grade is D")
# elif(marks >=0 and marks <40):
#     print("Fail*")

# ---------------------------

# odd or even program 
# a = int(input("Enter the number to check odd/even: "))
# oddoreven = a % 2
# if ( oddoreven == 0 ):
#     print("Even")
# else:
#     print("Odd")

# print(oddoreven)
# -------------------------

# largest among three numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter third number:"))
if(a >= b and a >= c and a >= d):
   print("Largest number is :", a) 
elif(b >= c and b >= d):
    print("Largest number is :", b)
elif(c >= d):
    print("Largest number is :", c)
else:
    print("Largest number is :", d)