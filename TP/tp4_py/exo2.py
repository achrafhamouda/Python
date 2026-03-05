mylist = [14, 16, 12, 19, 18]

# L'ajout des nouveaux notes 17 et 13 
mylist.append(17)
mylist.append(13)
print(f"La nouvelle liste est : {mylist}")

# Supression de la note la plus petite 
a = min(mylist)
mylist.remove(a)
print(f"La nouvelle liste apres la suppression de la note minimal est : {mylist}")

# Calcul de moyenne
moy = sum(mylist) / len(mylist)
moyenne = round(moy,2)
print(f"La moyenne des notes est : {moyenne}")

# tri de la liste en ordre decroissant
mylist.sort(reverse=True)
print(mylist)