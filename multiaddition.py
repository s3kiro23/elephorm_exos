print("Effectuer une multiplication de 2 entiers positifs en n'utilisant que l'addition")

a= int(input("Entrez votre 1ère valeur :"))
b= int(input("Entrez votre 2ème valeur :"))
res= 0


# Avec un While

while b != 0 :
    if a < 0 or b < 0 :
        print("Erreur, veuillez saisir 2 valeurs positives")
        a=int(input("Saisissez à nouveau une valeur pour a :"))
        b=int(input("Saisissez à nouveau une valeur pour b :"))
    else :
        b-=1
        res = a + res

print(res)


# Avec un For in

# for i in range(b) :
#     i = i + 1
#     res = a + res   

# print(res) 

    

