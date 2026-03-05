from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Wouf Wouf"
    
class Chat(Animal):
    def parler(self):
        return "Miaou"

a1 = Chien("bobi")
a2 = Chat("simba")

print(a1.nom, "dit :", a1.parler())
print(a2.nom, "dit :", a2.parler())

