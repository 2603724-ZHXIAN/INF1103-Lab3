def get_valid_input():
  user_input = input("Input quantity (or type 'quit' to finish): ").strip()
  if user_input.lower() == 'quit':
          return 'quit'
  elif not user_input.isdigit():
          print("Invalid input. Please enter a valid integer number.")
          return None
  elif user_input.startswith('-'):
          print("Invalid input. Please enter a valid integer number.")
          return None
  else:
       return user_input

def process_delivery(current_total, new_value):
    current_total += new_value
    return current_total

def calculate_tax(amount):
    return amount * 0.1

def float_valid_input():
    user_input = input("Input delivery amount: ").strip()
          
    try:
        # Attempt to convert the string to a float
        value = float(user_input)
        
        # Check if the float is a positive number
        if value < 0:
            print("Invalid input. Please enter a valid amount.")
            return None
            
        # Return the actual float so you can do math with it later
        return value
        
    except ValueError:
        # This triggers if the user types letters, symbols, or multiple decimals
        print("Invalid input. Please enter a valid amount.")
        return None

def generate_report(total_units, failed_attempts, count, current_total):
    print("\nInventory Audit Report")
    print("============================")
    print(f"Total Unit Quantity: {total_units}")
    print(f"Total Deliveries Processed: {count}")   
    print(f"Total Amount including Tax: {current_total}")
    print(f"Failed Attempts: {failed_attempts}")
    return True



#Initialize variables to keep track of total inventory and failed entries
total_inventory = 0
failed_entries = 0
current_total = 0
count = 0


print("Inventory Audit System")
print("----------------------")

while True:
    result = get_valid_input()
    if result == 'quit':
        generate_report(total_inventory, failed_entries, count, current_total)
        break
    elif result is None:
        failed_entries += 1
    elif result  is not None:
        check_maximum = int(result) + total_inventory
        if check_maximum > 500:
            print("Maximum inventory limit reached. Cannot add more units.")
            failed_entries += 1
            break
        count += 1
        total_inventory += int(result)
        while True:
            new_value = float_valid_input()
            if new_value is None:
                failed_entries += 1
            elif new_value is not None:
                break
        #Process the delivery amount and update the current value 
        current_total = process_delivery(current_total, new_value)

        #add the tax with the delivery amount to the current total
        current_total += calculate_tax(new_value)    
        








