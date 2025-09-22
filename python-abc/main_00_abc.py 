#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

# Création d'un chien et d'un chat
bobby = Dog()
garfield = Cat()

print(bobby.sound())     # Affiche "Bark"
print(garfield.sound())  # Affiche "Meow"

# Tentative de création d'un Animal (doit échouer)
try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(f"Erreur : {e}")
