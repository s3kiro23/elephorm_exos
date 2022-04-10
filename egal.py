## Aglo pour tester si un nombre est égale à un autre
import random

C1 = 15
C2 = 20
var1 = 0

while var1 != C1 and C2:
    var1 = int(input("Veuillez saisir un nombre :"))
    if var1 == C1 or var1 == C2:
        if var1 == C1:
            print("Le nombre saisi est égale à 15")
            break
        if var1 == C2:
            print("Le nombre saisi est égale à 20")
            break
    else:
        print("Le nombre saisi n'est pas égale à",C1,"ni à",C2)
print("Kek !")