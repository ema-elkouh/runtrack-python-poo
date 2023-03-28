class Animal: 
    def __init__(self):
        self.age=0
        self.nom=""

    def Vieillir(self):
        print(f"L'animal aura {self.age + 1} ans l'année prochaine")

    def nom(self):
        self.nom = nom
        print(f"Le nom de l'animal est {self.nom}")


animal = Animal()
animal.Vieillir()
animal.nom("lola")
animal.age=int(input("Quel age a l'animal ? "))
animal.Vieillir()