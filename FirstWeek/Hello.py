import math

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
#
# print('Hello ' + first_name + ' ' + last_name + '!')
# #anything after this gets ignored by python
#
# #using int will only work with integers, no decimal places
# hourly_wage = int(input("How much do you earn per hour?"))
#
# hourly_wage = float(input("How much do you earn per hour?"))
# print('You make: ', hourly_wage * 40 , 'per week' )
#
# #() for tuples, [] for lists, {} for dictionaries
# students_names = [ 'Mohamed', 'Jenny', 'Allen', 'Christie', 'Shafali' ]
#
# for student in students_names:
#     print(student)
#
# for index in range( len(students_names) ):
#     print(students_names[index])
#
# students_names.insert(2, "Bob")
# students_names.remove('Jenny')
# print(students_names)
#
# if 'Eric' in students_names:
#     print("Eric is here")
# elif 'Jenny' in students_names:
#     print("Jenny is here and Eric is not")
# else:
#     print("Eric and Jenny have left the building")
#
# grades = {
#     'Mohamed' : 'A',
#     'Jenny' : 'A',
#     'Allen' : 'A',
#     'Christie' : 'A',
#     'Shafali' : 'A'
# }
#
# if 'Mohamed' in grades:
#     print(grades['Mohamed'])
# else:
#     print("Not an A student")
#
# sorted_names = sorted(list(grades.keys()))
#
# for student in sorted_names:
#     print(student, ' grade: ', grades[student])
#
# for student, grade in grades.items():
#     print(student, grade)
#
# favorite_number = int(input("What is your favorite number?"))
#
# if favorite_number == 42:
#     print("You have the answer")
# else:
#     print("go read hitch hikers guide to the galaxy")
#
# print( 5 % 2 )
#
# primes = []
#
# for number in range(2,1000):
#     is_prime = True
#     divisor = 2
#     while is_prime and divisor < number:
#         if number % divisor == 0:
#             is_prime = False
#         divisor += 1
#         # divisor = divisor + 1
#     if is_prime:
#         print(number)
#         primes.append(number)
#
# # list/string slicing
# print(primes[::-1])
#
# alphabet = 'abcdefghijklmnopqrstuvwsxyz'
# print( alphabet[::2])
#

# start of 1/18
def find_largest( list_to_search ):
    largest = list_to_search[0]

    for index in range(1,len(list_to_search)):
        if list_to_search[index] > largest:
            largest = list_to_search[index]

    return largest

def find_smallest( list_to_search ):
    smallest = list_to_search[0]

    for index in range(1,len(list_to_search)):
        if list_to_search[index] < smallest:
            smallest = list_to_search[index]

    return smallest


def find_average( list_to_average ):
    return sum(list_to_average) / len(list_to_average)

def find_median( list_to_find_median ):
    sorted_list = sorted(list_to_find_median)

    # even length
    if len(sorted_list) % 2 == 0:
        middle_index_right_side = len(sorted_list) // 2
        middle_index_left_side = middle_index_right_side - 1

        # slow way
        return( sorted_list[middle_index_left_side] + sorted_list[middle_index_right_side] ) / 2

    else: # must be odd
        middle_index = len(sorted_list) // 2
        return sorted_list[middle_index], 10


def find_population_standard_deviation( list_to_find ):
    average = find_average(list_to_find)
    running_total_variance = 0
    for value in list_to_find:
        # same as ( running_total_variance = running_total_variance + (value - average)**2 )
        # ** is to the power of
        running_total_variance += (value - average)**2
    variance = running_total_variance / len(list_to_find)

    return math.sqrt(variance)

favorite_numbers_list = [ 13, 7, 9, 3, 8, 6 ]

print(find_largest(favorite_numbers_list))

print(find_smallest(favorite_numbers_list))

print( find_average(favorite_numbers_list) )

print( find_median( favorite_numbers_list))


def add_and_subtract( first_value, second_value ):
    add = first_value + second_value
    subtract = first_value - second_value

    return add, subtract


#addition_result, subtraction_result = add_and_subtract( 10, 15 )

#print("10 + 15 =", addition_result)
#print("10 - 15 =", subtraction_result)

result = add_and_subtract( 10, 15 )
print("10 + 15 =", result[0])
print("10 - 15 =", result[1])

add_and_subtract( second_value=15, first_value=10)

# default arguments
def print_the_date( month, day, year="2018"):
    month = "Jan"
    print(month + "/" + day + "/" + year)

month = "01"
print_the_date(month, "18")
print_the_date(month, "18", "2017")
print(month)


place_to_eat = ""
hungry_for_thai_food = True
if hungry_for_thai_food:
    place_to_eat = "Hang's Bistro"
else:
    place_to_eat = "McDonalds"

place_to_eat = "Hang's Bistro" if hungry_for_thai_food else "McDonalds"

evens = [number for number in favorite_numbers_list if number % 2 == 0]
squares = [number**2 for number in favorite_numbers_list ]
print(evens)
print(squares)