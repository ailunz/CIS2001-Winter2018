class Square:

    def __init__(self):
        self.length_of_side = 0

    def calculate_area(self):
        return self.length_of_side ** 2

    def calculate_perimeter(self):
        return self.length_of_side * 4