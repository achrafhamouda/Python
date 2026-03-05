class CompteBancaire:
    def __init__(self, titulaire, solde):
        self.titulaire = titulaire
        self._solde = solde   # attribut protégé

    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant
        else:
            print("Solde insuffisant")

    def afficher_solde(self):
        print("Solde :", self._solde, "DH")

    def __str__(self):
        return f"Compte de {self.titulaire} - Solde : {self._solde} DH"


c1 = CompteBancaire("Alice", 1700)
print(c1)

