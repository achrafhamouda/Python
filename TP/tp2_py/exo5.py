n = int(input("Entrer votre nombre : "))

def Est_parfait(x) :
    somme = 0
    for i in range(1,x) :
        if x % i == 0 :
            somme += i
    return somme == x

distance = 0

while True :
    if Est_parfait(n + distance) :
        print("Le plus proche parfait de n est ", n + distance)
       
        break
    elif Est_parfait(n - distance) :
        print("Le plus proche parfait de n est ", n - distance)
       
        break
    distance += 1