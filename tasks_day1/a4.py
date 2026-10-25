"""Ask for some details and display them using f-strings."""
import sys


def main():
    if len(sys.argv) >= 4:
        name = sys.argv[1]
        age = sys.argv[2]
        city = sys.argv[3]
    else:
        try:
            name = input("Enter your name: ").strip()
            age = input("Enter your age: ").strip()
            city = input("Enter your city: ").strip()
        except EOFError:
            name, age, city = "", "", ""

    name = name or "Kritika Shah"
    age = age or "22"
    city = city or "Kathmandu"

    print(f"\nHi, I'm {name}. I'm {age} years old and live in {city}.")
    print(f"Profile: {name.upper()} | {age} years old | {city.title()}")

if __name__ == "__main__":
    main()
