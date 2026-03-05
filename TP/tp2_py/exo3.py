# Vérifier si un nombre est palindrome - Méthode mathématique
a = int(input("Entrer votre nombre : "))
n = a
inverse = 0

while n > 0:
    d = n % 10           # Récupère le dernier chiffre
    inverse = inverse * 10 + d  # Ajoute ce chiffre à la fin de l'inverse
    n = n // 10          # Supprime le dernier chiffre

if a == inverse:
    print("Votre nombre est palindrome")
else:
    print("Votre nombre n'est pas palindrome")
    # Transformer la chaîne en son inverse inverse = a[::-1]
