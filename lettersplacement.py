import random
from re import M

## Avec For in

l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in l:
    i = i + 1
    a= input("Veuillez saisir une lettre :")
    if a > l[13]:
        print("Cette lettre se trouve après la lettre m")
    elif a == l[13]:
        print("Cette lettre correspond à la lettre de référence 'm', veuillez saisir une autre lettre")
    else:
        print("Cette lettre se trouve avant la lettre m")

## Avec While

count=random.choice(range(101))

while count > 0:
    print("Tentative restante =",count)
    a= str(input("Veuillez saisir une lettre :"))
    if l[a] > l.index("m"):
        print("Cette lettre se trouve après la lettre m")
    elif a == l.index("m"):
        print("Cette lettre correspond à la lettre de référence 'm', veuillez saisir une autre lettre")
    else:
        print("Cette lettre se trouve avant la lettre m")
    count-=1

        



