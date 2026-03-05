def kaprekar(x):
    if x == 1:
        print("Votre nombre est un Kaprekar")
        return

    y = x * x
    l = len(str(x))


    droite = y % (10 ** l)
    gauche = y // (10 ** l)

    if gauche + droite == x:
        print("Votre nombre est un Kaprekar")
    else:
        print("Votre nombre n'est pas un Kaprekar")

a = int(input("Entrer votre valeur : "))
kaprekar(a)
print("Les 10 premiers nombres de Kaprekar sont :")
count = 0
n = 1

while count < 10:
    y = n * n
    l = len(str(n))
    droite = y % (10 ** l)
    gauche = y // (10 ** l)

    if gauche + droite == n:
        print(n)
        count += 1
    n += 1