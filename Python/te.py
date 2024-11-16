
import random
hochste = int(input("Geb die höchste Zahl an"))
x = random.randint(0,hochste)
midde = hochste/2
print ("Random Number:")
print (x)

if x > midde:
    print ("yay, du hattest gluck")
    str(input()) 
else:
    print ("du hattest kein glück")
    str(input())
    