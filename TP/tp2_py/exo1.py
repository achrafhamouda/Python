import random
d = random.randint(1,100)
print("Vous avez seulement 10 tentative")
tentative = 10
while tentative > 0 :
    a = int(input("Entrer la valeur a deviner "))
    if a == d : 
        print("Vous avez reussit")
        break
    else : 
        tentative -= 1
        if tentative == 0 :  print("Vous avez echoue Ressayer plus tard")
        else :
            if a > d :
                print("Trop Grand")
                print("ressayer !")
                print(f"Vous avez encore {tentative} tentative")
                print("-----------------------------------------------")
            else : 
                print("Trop petit")
                print("ressayer !")
                print(f"Vous avez encore {tentative} tentative")
                print("-----------------------------------------------")