class Forme: 
    def __init__(self, aire=0):
        self.aire= aire

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

mon_rectangle = Rectangle(5,3)

print("L'aire du rectangle est ", mon_rectangle.aire())
