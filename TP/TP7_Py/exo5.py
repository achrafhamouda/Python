class Moteur:
    def __init__(self, puissance):
        self.puissance = puissance

    # Getter
    def get_puissance(self):
        return self.puissance

    # Setter
    def set_puissance(self, puissance):
        if puissance <= 0:
            raise ValueError("La puissance doit être positive")
        self.puissance = puissance

    def demarrer(self):
        print("Le moteur de", self.puissance, "CV démarre")

class Voiture:
    def __init__(self, marque, moteur):
        self._marque = marque
        self.moteur = moteur   # composition : Voiture A un Moteur

    # Getter
    def get_marque(self):
        return self._marque

    # Setter
    def set_marque(self, marque):
        self._marque = marque

    def demarrer_voiture(self):
        print("La voiture", self._marque, "démarre")
        self._moteur.demarrer()

class Garage:
    def __init__(self):
        self.voitures = []

    def ajouter_voiture(self, voiture):
        if not isinstance(voiture, Voiture):
            raise TypeError("Seules les voitures peuvent être ajoutées")
        self.voitures.append(voiture)

    def afficher_voitures(self):
        for v in self.voitures:
            print("Voiture :", v.get_marque())

class GaragePleinException(Exception):
    pass
