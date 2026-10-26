"""Assignment 1: Print even numbers from 1 to N."""


def get_valid_number():
    while True:
        try:
            value = input("Enter a positive integer N: ").strip()
            number = int(value)

            if number >= 1:
                return number

            print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def print_even_numbers():
    n = get_valid_number()
    print(f"\nEven numbers from 1 to {n}:")

    even_numbers = []
    for number in range(2, n + 1, 2):
        even_numbers.append(str(number))

    if even_numbers:
        print(" ".join(even_numbers))
    else:
        print("No even numbers in this range.")


if __name__ == "__main__":
    print_even_numbers()
