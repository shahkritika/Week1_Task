"""Assignment 3: Read 3 numbers as strings; print min, max, average to 2 decimals."""

def parse_float(prompt_text):
    while True:
        raw = input(prompt_text).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g. 10 or 3.14).")

def number_stats():
    print("=== 3-Number Statistics ===")
    
    # Reading numbers
    n1 = parse_float("Enter first number: ")
    n2 = parse_float("Enter second number: ")
    n3 = parse_float("Enter third number: ")
    
    nums = [n1, n2, n3]
    
    minimum = min(nums)
    maximum = max(nums)
    average = sum(nums) / len(nums)
    
    print("\n--- Results (formatted to 2 decimal places) ---")
    print(f"Minimum : {minimum:.2f}")
    print(f"Maximum : {maximum:.2f}")
    print(f"Average : {average:.2f}")

if __name__ == "__main__":
    number_stats()
