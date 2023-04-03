class Personne: 
    def __init__(self, age=14):
        self.age=age
    def AfficheAge(self):
        print("L'age de la personne est ", self.age)

    def Bonjour(self):
        print("Hello")

    def ModifierAge(self, NouvelAge):
        self.age = NouvelAge


class Eleve(Personne):

    def allerEnCours(self):
        print("Je vais en cours")

    def afficheAge(self):
        print("J'ai", self.age, "ans")

class Professeur():
    def __init__(self, matiereEnseignée):
      self.__matiereEnseignée=matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")


p = Personne()

print (p.age)

e = Eleve()

print(e.age)