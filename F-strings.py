# F strings--         string formatting in python--------
# here F means fast

import math
me = "dhruv"
al = 3
#a = "this is %s"%al
#print(a)


#a = "this is {} {}"
#b = a.format (me, al)
#print(b)
#a = f"this is {me} {al} {4*65}"
a = f"this is {me} {al} {math.cos(65)}"
print(a)