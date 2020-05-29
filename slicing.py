mystr = "dhruv is a CSE student"

print(len(mystr))
print(mystr[0:4])  # here 0 for including and 4 is for the excluding.
print(mystr[0:]) # here it will take all the words.
print(mystr[:5]) # here it will take 0 automatically for the starting place.
print(mystr[:]) # here it will take all the words.
print(mystr[::]) # here in the third place it will take automatically 1 and in the middle it will take full length no. and in the first it will take 0 automatically.
# in this we can see that the if we remove any of the no in it than it takes already fixed no.
# like Print(mystr[0::])
#      print(mystr[:19:])
#      print(mystr[::1]) here in  these three place we will get the same value.       
print(mystr[::2]) # in this it will miss the one by one character.
print(mystr[::3]) # in this it will miss the two characters after printing each word.

print(mystr[::7665]) # in this it will take only that value which is present. so this is called advamce sliciing.
"""
# now let's see the negative slicing
#print(mystr[-4:-2])


#functions_________-

#print(mystr.isalnum()) # it shows the alpha numeric value and it gives answer in the boolean function like true or false.
print(mystr.endswith("student")) # it gives output true bcz here we cam see that the string is ending with the student word.
print(mystr.count("d")) # it gives the output by counting word which we want.
print(mystr.capitalize()) # it will do capitalize our string.
print(mystr.find("is")) # it shows the starting no. of given word.
print(mystr.lower())
print(mystr.upper()) # it will do the all the elements in the upper case.
print(mystr.replace("is", "are"))
"""