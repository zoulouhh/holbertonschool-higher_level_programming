#!/usr/bin/python3
# Définition de la classe Square (Carré)
class Square:
     # Méthode spéciale appelée lors de la création d'une instance de Square
    def __init__(self, size):
        # Attribut d'instance privé qui stocke la taille du carré
        # Le double underscore rend l'attribut privé (non accessible directement)
        self.__size = size

