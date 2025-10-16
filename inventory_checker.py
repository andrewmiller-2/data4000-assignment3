def get_validated_input(prompt, target_type):
    """Handles continuous prompting and validation."""
    while True:
        try:
            user_input = input(prompt)
            value = target_type(user_input)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a number.")

current_inv = get_validated_input("Enter current inventory: ", int)
min_order = get_validated_input("Enter minimum reorder level: ", int)

if current_inv < min_order:
    print("Order more inventory")
else:
    print("Inventory level is sufficient")

try:
    inventory_percentage = (current_inv / min_order) * 100
    # FIX: Added the closing quote and changed to an f-string for correct formatting
    print(f"Inventory is at {inventory_percentage:.2f}% of the minimum reorder level")
except ZeroDivisionError:
    print("Minimum reorder level cannot be zero.")