class Forme: 
    def __init__(self, aire=0):
        self.aire= aire

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(Cercle):
        return 3.14 * (self.radius)**2
    

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur


cercle = Cercle(5)
rectangle = Rectangle(4, 6)

print("Aire du cercle:", cercle.aire())
print("Aire du rectangle:", rectangle.aire())



    