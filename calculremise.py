print("Algorithme pour le calcul d'une remise")

n= int(input("Entrez votre montant supérieur ou égale à 2000 euros :"))
rem1= 0.05
rem2= 0.10
fourch1= 2000
fourch2= 5000
res= 0


    
# while res == 0 :
#     if n >= fourch1 and n <= fourch2 :
#         res = n - n * rem1
#         print("Voici votre montant net après application de la réduction à 5% = ",res,"euros")
#     else :
#         if n > fourch2 :
#             res = n - n * rem2
#             print("Voici votre montant net après application de la réduction à 10% =",res,"euros")
#         elif n < fourch1 :
#             print("Veuillez saisir un montant supérieur à 2000 euros !")
#             n= int(input("Entre votre nouveau montant :"))

## Correction Exo

if n < fourch1 :
    res = n
    print("Aucune remise disponible pour ce montant")

else :
    if n <= fourch2 :
        res = n - n * rem1
        print("Voici votre montant net après application de la réduction à 5% = ",res,"euros")
    else :
        res = n - n * rem2
        print("Voici votre montant net après application de la réduction à 10% =",res,"euros")
