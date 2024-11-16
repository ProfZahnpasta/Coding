import random

lol = random.randint(0,1)

print ("Deine Zahl ist:")
print (lol)

if lol < 1:
    print ("Du hast verloren")
else:
    print ("Du hast gewonnen!")
    
int(input())