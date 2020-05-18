print("what is your age?")
age = int(input())  

if age > 18:
    print("yes, you are eligible for the driving")
elif age == 18:
    print("you can drive") 
#elif age < age_limit:
#    print("you are not eligible for driving")
else:
    print("no, you can't drive")