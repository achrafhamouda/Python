message = "Apprendre Python est amusant et utile !"

#  Mettre la première lettre de chaque mot en majuscule
maj = message.title()
print("Première lettre de chaque mot en majuscule :",maj)

# Trouver combien de fois le mot 'et' apparaît
nbr_et = message.lower().count("et")
print("Nombre d'occurrences de 'et' est :", nbr_et)

# Vérifier si la chaîne commence par 'Apprendre'
debut = message.startswith("Apprendre")
print("La phrase commence par 'Apprendre' :", debut)

# Inverser la casse des lettres
inv = message.swapcase()
print("Casse inversée :",inv)