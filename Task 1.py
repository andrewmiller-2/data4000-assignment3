def get_validated_input(prompt, target_type):
    """Handles continuous prompting and validation."""
    while True:
        try:
            user_input = input(prompt)
            value = target_type(user_input)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a number.")

# --- Main Program ---

# 1. Get valid units (integer)
units_sold = get_validated_input("Units Sold (int): ", int)

# 2. Get valid price (float)
unit_price = get_validated_input("Unit Price (float): ", float)

# 3. Calculate and print total
total_revenue = units_sold * unit_price
print("Total Price: $", total_revenue)
