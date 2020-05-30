# exception handling---------

# mostly these thing we uses at that time like when user have a problem of internet connectivity
   #so there we will use this for printing the error


print("Enter num 1")
num1 = input ()
# num1 = int(input())
print("Enter num 2")
num2 = input ()
#num2 = int(input())
try:
    print("The sum of these two numbers is",
          int(num1) + int(num2))
except Exception as e:
    print(e)          

print("this line is very imporatnt")    