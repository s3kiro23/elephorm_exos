## Algo de tri croissant entre 3 nombres

v1 = int(input("Veuillez saisir votre 1ère valeur :"))
v2 = int(input("Veuillez saisir votre 2ème valeur :"))
v3 = int(input("Veuillez saisir votre 3ème valeur :"))
tmp = 0

if v1 > v2 :
    tmp = v1
    v1 = v2
    v2 = tmp
if v3 < v1 :
    tmp = v1
    v1 = v3
    v3 = v2
    v2 = tmp
else:
    if v3 < v2 :
        tmp = v2
        v2 = v3
        v3 = tmp

print(v1,v2,v3)

