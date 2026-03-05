def somme_chiffres(x):
    somme = 0
    for a in str(x):
        somme += int(a)
    return somme

def palindrome(n):
    inverse = 0
    temp = n
    while temp > 0:
        d = temp % 10
        inverse = inverse * 10 + d
        temp //= 10
    return inverse

n = int(input("Entrer votre nombre : "))
iteration = 0

while True:
    if n == palindrome(n):
        print("Le nombre palindrome obtenu est :", n)
        print("Nombre d'itérations nécessaires :", iteration)
        break

    else:
        n += somme_chiffres(n)
        iteration += 1
        print(f"Étape {iteration} → Nouveau nombre = {n}")
