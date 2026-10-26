"""Assignment 4: Convert Celsius (string input) to Fahrenheit.
Formula: F = (C * 9/5) + 32
"""

def celsius_to_fahrenheit():
    print("=== Celsius to Fahrenheit Converter ===")
    
    while True:
        celsius_str = input("Enter temperature in Celsius (°C): ").strip()
        try:
            celsius = float(celsius_str)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical temperature value.")

    # Conversion formula
    fahrenheit = (celsius * 9.0 / 5.0) + 32.0

    print("\n--- Output ---")
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")

if __name__ == "__main__":
    celsius_to_fahrenheit()
