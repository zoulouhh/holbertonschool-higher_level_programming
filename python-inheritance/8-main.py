#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

if __name__ == "__main__":
    # Création d'une instance Rectangle valide
    r1 = Rectangle(10, 5)
    print(f"Rectangle width: {r1._Rectangle__width}")
    print(f"Rectangle height: {r1._Rectangle__height}")

    # Essai avec des valeurs invalides (doit lever une exception)
    try:
        r2 = Rectangle(-3, 4)
    except Exception as e:
        print(e)

    try:
        r3 = Rectangle(3, "4")
    except Exception as e:
        print(e)
