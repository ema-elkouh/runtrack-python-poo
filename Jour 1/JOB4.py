class Personne: 
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


    def sePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")


p1 = Personne ("Dupont", "Jean")
p2 = Personne ("El kouh", "Ema")

p1.sePresenter()
p2.sePresenter()

