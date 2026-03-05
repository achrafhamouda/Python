def nbr_parfait(x) :
    somme = 0
    for i in range(1,x) :
        if x % i == 0 :
            somme += i
    return somme == x
nombre = 1
compt = 0
while compt < 5 :
    if nbr_parfait(nombre) :
        print(nombre)
        compt +=1
    
    nombre += 1