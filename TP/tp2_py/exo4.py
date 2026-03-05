n = int(input("Entrer votre nombre : "))
bas = 0
haut = n
center = 0

while bas <= haut :
    center = ( bas + haut ) // 2
    if (center * center) == n : 
        print("La racine entiere est", center)
        break
    else :
        if center * center > n :
            haut = center - 1
    
        else : 
            bas = center + 1