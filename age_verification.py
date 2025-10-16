def get_customer_age():
    """
    Uses a while True loop to repeatedly prompt for a customer's age.
    Handles ValueError if non-integer input is provided.
    Returns a valid, positive integer age.
    """
    while True:
        try:
            age_input = input("Enter customer's age: ")
            age = int(age_input)

            if age > 0:
                return age
            else:
                print("Age must be a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

# --- Main Program ---
ELIGIBILITY_AGE = 18

try:
    customer_age = get_customer_age()
    
    # Determine eligibility
    if customer_age >= ELIGIBILITY_AGE:
        print(f"Customer is {customer_age}. Eligible for promotion.")
    else:
        print(f"Customer is {customer_age}. NOT eligible (must be {ELIGIBILITY_AGE}+).")

# Handles a variable being referenced without being defined (e.g., if ELIGIBILITY_AGE was commented out)
except NameError:
    print("ERROR: A required configuration variable (eligibility age) is missing.")

except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
