class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
    def get_longueur(self):
        return self._longueur
    def set_longueur(self):
        return self.longueur
    
    def get_largeur(self):
        return self.largeur(self)
    def set_largeur(self):
        return self.largeur(self)
    
    def perimetre(self):
        return 2 * (self._longueur + self.get_largeur)
    
    def surface(self):
        return  self.get_longueur * self.get_largeur
    
class Parallélépipède(Rectangle): 
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def set_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hasattr
    def volume (self):
        return self.surface() * self.__hauteur
    
