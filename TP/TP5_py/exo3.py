fruits = {"pomme", "banane", "orange", "kiwi"}

fruits.add('mangue')
print(fruits)

fruits.remove('kiwi')
print(fruits)

fruits.discard('fraise')
print(fruits)

tropiques = {"banane", "mangue", "ananas", "papaye"}
v = fruits.difference(tropiques)
print(v)

c = fruits.difference_update(tropiques)
print(c)

print(f"fruits après la mise à jour ",fruits)

fruits_verts = {"pomme", "kiwi", "poire"}

inter = fruits_verts.intersection(fruits)
print(inter)

uni = fruits_verts.union(fruits)
print(uni)

z = fruits_verts.isdisjoint(fruits)
print(z)

x = fruits_verts.issuperset(fruits)
print(x)

m = fruits_verts.issubset(uni)
print(m)

n = fruits.pop()
print(f"Le nombre aleatoire a supprimer est :",n)
print(f"La nouvelle set : ",fruits)