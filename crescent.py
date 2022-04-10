## Algo pour afficher si 3 variables sont rangées par ordre croissant ou non

var1 = int(input("Saisissez votre 1ère valeur :"))
var2 = int(input("Saisissez votre 2ème valeur :"))
var3 = int(input("Saisissez votre 3ème valeur :"))

if var1 < var2 and var2 < var3:
    print(var1,var2,var3,"Ces valeurs sont rangées par ordre croissant")
else:
    print(var1,var2,var3,"Ces valeurs ne sont pas rangées par ordre croissant")