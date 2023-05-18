# Write a Python function that takes a non-negative integer as input
# and returns the digits of the number in reverse order as a list.

number = 12345
def reverse_digits(number):
    digits = []  # Create an empty list to store the reversed digits
    string = str(number)  # Convert the number to a string

    for digit in string:
        digit = int(digit)  # Convert the character to an integer
        digits.append(digit)

    return digits[::-1]


print(reverse_digits(number))
