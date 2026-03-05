etudiant = {
"nom": "Sara",
"age": 20,
"note": 17,
"classe": "IACS"
}

a = etudiant.get("note")
print(a)

b = etudiant.get("adress","Non renseignée")
print(b)

c = etudiant.keys()
print(c)

d = etudiant.values()
print(d)

#print(etudiant.items())
for cle ,valeur in etudiant.items():
    print(cle,":",valeur)

etudiant["note"] = 18
print(etudiant)

etudiant["email"] = "alice@example.com"
print(etudiant)

etudiant.update({"ville": "Casablanca", "tel":
"0612345678"})
print(etudiant)

etudiant.pop("classe")
print(etudiant)

etudiant.pop("poly",121)
print(etudiant)

print("nom" in etudiant)

j = len(etudiant)
print(j)

l = etudiant.copy()
print(l)

h = etudiant.clear()
print(h)