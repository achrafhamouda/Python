a = int(input("Entrer un nombre a positif : "))
b = int(input("Entrer un nombre b positif : "))

if b == 0 : print("Impossible")
elif a == 0 : print("La division entiere = 0")
elif b > a : print("La division entiere = 0")

z = 1
while b * z <= a :
    quotient = z
    z += 1
print("La division entiere de",a," par ",b, "est ",quotient)

