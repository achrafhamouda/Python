a = int(input("Entrer un nombre a : "))
b = int(input("Entrer un nombre b : "))
n = int(input("Entrer votre nombre n : "))

if n == 1:
    print(a)
elif n == 2:
    print(b)

else :
    f1 = a
    f2 = b
    c = 3
    while c <= n :
        fc = f1*f1 + f2*f2
        f2 = f1
        f1 = fc 
        c += 1
    print(fc)

