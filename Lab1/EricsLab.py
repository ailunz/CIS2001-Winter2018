choice = ""

def fahrenheit_to_celsius( fahrenheit ):
    return ( fahrenheit - 32 ) * 5 / 9

def celsius_to_fahrenheit( celsius ):
    return ( celsius * 9 / 5 ) + 32

def number_of_payments( monthly_rate, payment_amount, loan_balance ):
    current_balance = loan_balance

    if monthly_rate >= 1:
        monthly_rate /= 100
        # combined assignment is the same as
        # monthly_rate = monthly_rate / 100

    payments = 0
    while current_balance > 0:
        payments += 1
        current_balance += current_balance * monthly_rate
        current_balance -= payment_amount

    return payments

def calculate_payment_amount( monthly_rate, number_of_payments, loan_balance ):
    if monthly_rate >= 1:
        monthly_rate /= 100

    payment = ( monthly_rate * loan_amount ) \
              / ( 1 - ( 1 + monthly_rate )**-number_of_payments)

    return payment

while choice != "5":
    print("Welcome to lab 1, please select an option:")
    # Use multiple prints, or in the input use \n for newline
    #print("1 - Convert Fahrenheit to Celsius")
    #print("2 - Convert Celsius to Fahrenheit")
    #print("3 - Calculate number of payments needed given a rate and amount")
    #print("4 - Calculate the payment requirement given a rate and number of payments")
    #print("5 - Quit")
    choice = input("1 - Convert Fahrenheit to Celsius\n"
                   "2 - Convert Celsius to Fahrenheit\n"
                   "3 - Calculate number of payments needed given a rate and amount\n"
                   "4 - Calculate the payment requirement given a rate and number of payments\n"
                   "5 - Quit\n")

    print("You chose:", choice)

    if choice == "1":
        temp_in_fahrenheit = float(input("Enter the temp is Fahrenheit: "))
        print( fahrenheit_to_celsius( temp_in_fahrenheit ))
    elif choice == "2":
        temp_in_celsius = float(input("Enter the temp is Celsius: "))
        print(celsius_to_fahrenheit(temp_in_celsius))
    elif choice =="3":
        monthly_rate = float(input("Enter the APR of the loan: ")) / 12
        payment_amount = float(input("Enter the monthly payment amount: "))
        loan_amount = float(input("Enter the loan amount: "))
        # using named arguments vs positional
        print( "It will take",
               number_of_payments( loan_balance=loan_amount, payment_amount=payment_amount, monthly_rate=monthly_rate)
               , "payments to pay off the loan")

        # position arguments would be like this
        # number_of_payments( monthly_rate, payment_amount, loan_amount )
    elif choice == "4":
        monthly_rate = float(input("Enter the APR of the loan: ")) / 12
        number_of_payments = float(input("Enter the number of payments to be made: "))
        loan_amount = float(input("Enter the loan amount: "))
        print(calculate_payment_amount(monthly_rate, number_of_payments, loan_amount) )
    elif choice != "5":
        print("PLease enter a number 1-5")