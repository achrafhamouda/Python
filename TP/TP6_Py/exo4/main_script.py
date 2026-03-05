import json

with open("data.json", "r") as file:
    data = json.load(file)

# on affichage les noms
for employe in data["employees"]:
    print(employe["name"], " ", employe["position"])

# on ajout un nv employe
nv_employe = {"name": "achraf", "age": 19, "position": "PenTester"}
data["employees"].append(nv_employe)

# apres on affiche les noms
print("Fichier apres ajout")
for employe in data["employees"]:
    print(employe["name"])

# en fin on sauvegarde les modifs
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


