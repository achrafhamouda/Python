# Création de la liste
my_list = list(range(1,11,1))
print(my_list)

# Ajout de 11 et 12
my_list.append(11)
my_list.append(12)
print(my_list)

# Insertion de 0 au début
my_list.insert(0, 0)
print(my_list)

# Supprimer le dernier élément
my_list.pop()
print(my_list)

# Trouvants l’indice de 5
idx = my_list.index(5)
print(f"Indice de 5 : {idx}")

# Multiplier chaque élément par 2
for a in my_list :
    my_list[a] *= 2 
print("Liste multipliée par 2 :", my_list)

###########################################

# Liste de fruits
fruits = ["pomme", "banane", "orange", "kiwi", "mangue"]

# Trier par ordre alphabétique
fruits.sort()
print("Fruits triés :", fruits)

# Ajouter un nouveau fruit
fruits.append("limouna")
print(fruits)

# Vérifier si "kiwi" est dans la liste
if "kiwi" in fruits:
    print("'kiwi' est bien dans la liste.")
else:
    print("'kiwi' n'est pas présent dans la liste.")

fruit_rm = str(input("Entrer une fruit a supprimer : "))

if fruit_rm in fruits:
    fruits.remove(fruit_rm)
else:
    print(f"{fruit_rm} n'existe pas dans la liste.")

print("Liste finale des fruits :", fruits)