class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur= longueur 
        self.__largeur= largeur

    def get_longueur():
        return self.__longueur
    
    def set_longueur():
        return self.__longueur
    
    def get_largeur():
        return self.__largeur
    
    def set_largeur():
        return self.__largeur
    

rect= Rectangle (10, 5)

print(f"longueur: {rect.get_longueur}, largeur: {rect.get_largeur}")

#Pour changer la longueur ou la largeur :

rect.set_longueur(7)

# Affichage des attributs du rectangle modifiés
print(f"Longueur : {rect.get_longueur()}, Largeur : {rect.get_largeur()}")