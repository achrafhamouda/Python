a = input("Entrer votre nombre : ")
b = len(str(a))
print(b)
somme = 0

for c in a :
    somme += pow(int(c),b)

if somme == int(a) :
    print("Votre nombre est Armstrong")
else :
    print("Votre nombre est non Armstrong")