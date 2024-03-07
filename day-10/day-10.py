# exercise 1
def format_name(name1, name2):
    """Converting the first letter of the name1 and name2 names,
    to title names"""
    farst_name = name1.title()
    last_name = name2.title()
    return f"{farst_name} {last_name}"

# print(format_name("ali", "nazer"))

# exercise 2


def is_leap(year):
    """It calculates whether the year
       is a leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """It calculates the number of days in a month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 and month < 1:
        return "invalid month"
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide}
def calculator():
    num1 = float(input("What's the first number: "))
    for kay in operations:
        print(kay)
    should_continue = True
    while should_continue:
        opr = input("Pick on operation ")
        num2 = float(input("What's your second number: "))
        function_calculator = operations[opr]
        answer = function_calculator(num1, num2)

        print(f"{num1} {opr} {num2} = {answer}")
        ask = input(f"Type 'y' to continue calculating with or type 'n' to start a new calculating,  or type 'e' to exit ")
        if ask == "y":
            num1 = answer
        if ask == "n":
            should_continue = False
            calculator()
        if ask == "e":
            should_continue = False     
calculator() 

    