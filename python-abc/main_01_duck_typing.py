#!/usr/bin/env python3

from task_shapes import Shape, Circle, Rectangle, shape_info

def main():
    c = Circle(5)
    print("Circle:")
    shape_info(c)
    print()

    r = Rectangle(4, 6)
    print("Rectangle:")
    shape_info(r)
    print()

if __name__ == "__main__":
    main()
