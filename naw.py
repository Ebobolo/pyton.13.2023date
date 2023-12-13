#задачи номер 2

#№1
# def display_day(day):

#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     if day < 1 or day > 7:
#         print("Invalid day")
#     else:
#         print(days[day - 1])
#
# day = int(input("Enter the number of the day of the week from the keypad (1-7): "))
#
# display_day(day)
#_________________________________________________________________________________________
#№2
# import calendar
#
# def month_name(month_number):
#     return calendar.month_name[month_number]
#
# month_number = int(input("Enter the month number: "))
#
# print("The name of the month is:", month_name(month_number))
#________________________________________________________________________________________________
#№3
# def main():
#     number = float(input("Enter a number: "))
#     if number > 0:
#         print("Number is positive")
#     elif number < 0:
#         print("Number is negative")
#     else:
#         print("Number is equal to zero")
#
# if __name__ == "__main__":
#     main()
#__________________________________________________________________________________________
#№4
# def check_numbers(num1, num2):
#     if num1 == num2:
#         return f"Both numbers are equal: {num1}"
#     else:
#         ascending_order = sorted([num1, num2])
#         return f"The numbers in ascending order are: {ascending_order}"
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
#
# result = check_numbers(num1, num2)
#
# print(result)
#_____________________________________________________________________________________________________________________
#задачи номер 3
#№1
# def fizz_buzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "Fizz Buzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return str(number)
#
# while True:
#     try:
#         number = int(input("Enter a number between 1 and 100: "))
#         if 1 <= number <= 100:
#             print(fizz_buzz(number))
#         else:
#             print("Error: The number must be between 1 and 100.")
#     except ValueError:
#         print("Error: The input must be a number.")
