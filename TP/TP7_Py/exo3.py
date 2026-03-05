class Employe:
    def __init__(self, nom):
        self.nom = nom

    def calculer_salaire(self):
        return 0
class EmployePermanent(Employe):
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire

    def calculer_salaire(self):
        return self.salaire
class EmployeTemporaire(Employe):
    def __init__(self, nom, nombre_heures, tarif_horaire):
        self.nom = nom
        self.nombre_heures = nombre_heures
        self.tarif_horaire = tarif_horaire

    def calculer_salaire(self):
        return self.nombre_heures * self.tarif_horaire

e1 = EmployePermanent("yousra", 0)
e2 = EmployeTemporaire("achraf", 60, 39)

print("Salaire de", e1.nom, ":", e1.calculer_salaire(), "DH")
print("Salaire de", e2.nom, ":", e2.calculer_salaire(), "DH")

