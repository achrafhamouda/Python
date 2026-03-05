import math

a = float(input("Entrer la valeur de a : "))
b = float(input("Entrer la valeur de b : "))
c = float(input("Entrer la valeur de c : "))

if a == 0:
    print("Ce n'est pas une équation du 2e degré.")
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print(f"Deux solutions réelles distinctes : x1 = {x1} et x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Une seule solution réelle double : x = {x}")
    else:
        print("Pas de solution réelle (Δ < 0).")
