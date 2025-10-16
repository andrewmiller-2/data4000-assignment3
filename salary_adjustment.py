def get_valid_float_input(prompt):

    while True:
        try:
            user_input = input(prompt)
            # Attempt conversion to float
            value = float(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
        except Exception:
            print("An unexpected error occurred during input.")

def simulate_salary_adjustment():


    # 1. Get validated salary (using the helper function)
    current_salary = get_valid_float_input("Enter current salary ($): ")
    
    # Ensure salary is non-negative
    while current_salary < 0:
        print("Salary cannot be negative. Please try again.")
        current_salary = get_valid_float_input("Enter current salary ($): ")


    # 2. Get validated adjustment percentage
    while True:
        try:
            adjustment_percent = get_valid_float_input("Enter adjustment percentage (e.g., 5.0 for a 5% raise): ")

            # Custom check for negative percentage
            if adjustment_percent < 0:
                # We can handle this as a logical error, similar to a ZeroDivisionError,
                # by printing a message and forcing the loop to restart.
                print("Adjustment percentage cannot be negative. Please enter a percentage (0 or greater).")
                continue 

            # Break the validation loop if the percentage is valid (non-negative float)
            break

        except Exception as e:
            # Catch unexpected errors during the percentage process
            print(f"An error occurred: {e}. Please re-enter the percentage.")

    # --- Calculation (Executes only after all inputs are validated) ---

    # Convert percentage to a multiplier (e.g., 5.0 -> 0.05)
    multiplier = adjustment_percent / 100.0
    
    # Calculate the new salary
    new_salary = current_salary * (1 + multiplier)

    # --- Output ---
    print("\n--- Adjustment Summary ---")
    print(f"Old Salary: ${current_salary:,.2f}")
    print(f"Adjustment: {adjustment_percent:.2f}%")
    print(f"New Salary: ${new_salary:,.2f}")

# Execute the main function
if __name__ == "__main__":
    simulate_salary_adjustment()