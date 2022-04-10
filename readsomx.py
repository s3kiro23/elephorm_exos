nb1 = int(input("Veuillez saisir votre 1er nombre :"))
nb2 = int(input("Veuillez saisir votre 2ème nombre :"))
x = input("Saisissez une lettre :")
res=0

if x == "S":
    res = nb1 + nb2
    print(res)
else:
    res = nb1*nb2
    print(res)