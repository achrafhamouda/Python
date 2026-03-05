n = int(input("Entrer votre nombre : "))
iteration = 0
while n != 1 :
    iteration +=1
    if n % 2 == 0 :
        n = n // 2
        print("Iterartion : ",iteration," ; n = ", n)
    else :
        n = (n * 3) + 1 
        print("Iterartion : ",iteration," ; n = ", n)
    