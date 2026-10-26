"""Assignment 2: Keep asking for numbers until 0, then print the sum."""

def sum_until_zero():
    total_sum = 0.0
    count = 0
    
    print("=== Number Accumulator ===")
    print("Enter numbers one by one. Enter 0 (or 'O') to stop and calculate total sum.\n")
    
    while True:
        raw_val = input("Enter number: ").strip()
        
        
        if raw_val in ("0", "O", "o"):
            break
            
        try:
            num = float(raw_val)
            total_sum += num
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid number or 0 to finish.")

    print("\n--- Summary ---")
    print(f"Total numbers entered : {count}")
    
    if total_sum.is_integer():
        print(f"Total Sum            : {int(total_sum)}")
    else:
        print(f"Total Sum            : {total_sum:.4f}")

if __name__ == "__main__":
    sum_until_zero()
