with open("students.txt", "r") as f:
    lignes = f.readlines()

# ici on afficher chaque ligne
for ligne in lignes:
    print(ligne.strip())

# ici on extrait les notes
notes = []
for ligne in lignes:
    nom, note = ligne.split(",")   # on separe le nom et la note
    notes.append(int(note))

moyenne = sum(notes) / len(notes)

# ici on ecrirt la moy dans le fichier
with open("average.txt", "w") as f:
    f.write(f"Moyenne des notes : {moyenne:.2f}")


