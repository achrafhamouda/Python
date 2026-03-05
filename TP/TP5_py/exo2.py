notes=(12,15,18,10,15,18,17,20)

cpt = notes.count(15)
print(cpt)

idx = notes.index(18)
print(idx)

ordred = sorted(notes)
print(ordred)

print(max(notes))
print(min(notes))

print(14 in notes)

summ = sum(notes)
print(summ)

a = len(notes)
moy = summ/a
print(moy)

etudiants = (("Houda", 17), ("Ahmed", 12), ("Abdo", 19),
("Salma", 14))

hi_list = sorted(etudiants,key = lambda x : x[1] ,reverse = True)
print(hi_list)

top_etud = max(etudiants,key = lambda x :x[1])
print(top_etud)