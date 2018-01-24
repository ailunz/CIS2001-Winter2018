# this lets me just use Square() instead of Square.Square()
# from is the Module name ( file name ), import is the class name
from Square import Square

def print_square_stats( square ):
    print("a square with length of", square.length_of_side,
          "has an area of", square.calculate_area(),
          "and a perimeter of", square.calculate_perimeter())

# Square() calls the __init__ method
square_1 = Square()
square_1.length_of_side = 10

square_2 = Square()
square_2.length_of_side = 12

square_3 = Square()
square_3.length_of_side = 15

print_square_stats(square_1)
print_square_stats(square_2)
print_square_stats(square_3)


