"""Read a number and show it as a string, float, and integer."""
import sys


def main():
    if len(sys.argv) > 1:
        number_text = sys.argv[1]
    else:
        try:
            number_text = input("Enter a number (for example, 42.75): ").strip()
        except EOFError:
            number_text = ""

    if not number_text:
        number_text = "42.75"
        print(f"No number entered, so we'll use {number_text}.")

    number_as_string = str(number_text)
    number_as_float = float(number_text)
    number_as_int = int(number_as_float)

    print(f"\nAs a string:  {number_as_string} ({type(number_as_string).__name__})")
    print(f"As a float:   {number_as_float} ({type(number_as_float).__name__})")
    print(f"As an integer: {number_as_int} ({type(number_as_int).__name__})")

if __name__ == "__main__":
    main()
