class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print("Bonjour, je m'appelle", self.nom, "et j'ai", self.age, "ans")

p1 = Personne("achraf", 19)
p2 = Personne("yousra", 21)

p1.se_presenter()
p2.se_presenter()

