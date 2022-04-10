import random

## Algo3    

C1= 20
C2= 30
count=random.choice(range(101))
print("Nombre de tentatives =",count)

while count > 0 :
    x= int(input("Saisissez une nouvelle valeur :"))
    count-=1
    if x > C1 and x < C2:
        print("Le nombre saisi est compris entre",C1,"et",C2)
    else:
        print("Le nombre saisi n'est compris entre",C1,"et",C2)
    print("Nombre de tentatives restantes =",count)

