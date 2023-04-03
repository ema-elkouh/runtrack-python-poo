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
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        print("Je vais en cours")

    def afficheAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignée):
      super().__init__()
      self._matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("Le cours va commencer")

eleve1 = Eleve()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.ModifierAge(15)
eleve1.afficheAge()

prof1 = Professeur("Français")
prof1.ModifierAge(40)
print("Le professeur va commencer son cours de", prof1._Professeur__matiereEnseignée) 