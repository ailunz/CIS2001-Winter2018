choice = ""

def fahrenheit_to_celcius( fahrenheit ):
    return 0

def celcius_to_fahrenheit( celcius ):
    return 0




while choice != "5":
    print("Welcome to lab 1, please select an option:")
    # Use multiple prints, or in the input use \n for newline
    #print("1 - Convert Fahrenheit to Celcius")
    #print("2 - Convert Celcius to Fahrenheit")
    #print("3 - Calculate number of payments needed given a rate and amount")
    #print("4 - Calculate the payment requirement given a rate and number of payments")
    #print("5 - Quit")
    choice = input("1 - Convert Fahrenheit to Celcius\n"
                   "2 - Convert Celcius to Fahrenheit\n"
                   "3 - Calculate number of payments needed given a rate and amount\n"
                   "4 - Calculate the payment requirement given a rate and number of payments\n"
                   "5 - Quit\n")

    print("You chose:", choice)


    if choice == "1":
        temp_in_fahrenheit = input("Enter the temp is Fahrenheit: ")
        print( fahrenheit_to_celcius( temp_in_fahrenheit ))
    elif choice == "2":
        