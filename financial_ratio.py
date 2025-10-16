def calculate_profit_margin():
    """
    Prompts for profit and revenue, handling exceptions and looping
    indefinitely until a valid calculation is performed.
    """
    print("\n--- Profit Margin Calculator ---")
    
    # Loop indefinitely until valid inputs lead to a successful calculation
    while True:
        try:
            # 1. Get and convert inputs (potential ValueError here)
            profit_input = input("Enter Total Profit ($): ")
            revenue_input = input("Enter Total Revenue ($): ")
            
            profit = float(profit_input)
            revenue = float(revenue_input)

            # 2. Check for the division condition (potential ZeroDivisionError here)
            if revenue == 0:
                # Manually raise ZeroDivisionError to send control to the except block
                raise ZeroDivisionError 

        except ValueError:
            # Minor error (non-numeric input). Use 'pass' for silent reprompting.
            print("Invalid input. Please enter numeric values for profit and revenue.")
            continue # Skip to the next loop iteration

        except ZeroDivisionError:
            # Specific error handling for revenue being zero.
            print("ERROR: Revenue cannot be zero. Please enter a positive revenue amount.")
            pass

        else:
            # 3. This block executes ONLY if the 'try' block completed successfully (no exceptions)
            profit_margin = (profit / revenue) * 100
            print(f"Profit: ${profit:,.2f}")
            print(f"Revenue: ${revenue:,.2f}")
            print(f"Profit Margin Ratio: {profit_margin:.2f}%")
            break

# Execute the function
if __name__ == "__main__":
    calculate_profit_margin()