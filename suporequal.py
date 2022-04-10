## Afficher la plus grandes des 2 valeurs et retourner si égale ou pas avec une bool

from xmlrpc.client import boolean


x = int(input("Saisissez votre 1ère valeur :"))
y = int(input("Saisissez votre 2ème valeur :"))
sup = 0
bool=True

if x == y :
    bool=False
else:
    if x > y:
        sup += x
    else:
        sup += y
if bool :
    print("Le plus grand nombre est",sup)
else:
    print("Les deux nombres sont égaux")