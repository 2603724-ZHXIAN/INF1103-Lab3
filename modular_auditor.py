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
    print(amount * 0.1)
    return amount * 0.1


#Initialize variables to keep track of total inventory and failed entries
total_inventory = 0
failed_entries = 0
current_total = 0


print("Inventory Audit System")
print("----------------------")

while True:
    result = get_valid_input()
    if result == 'quit':
        break
    elif result is None:
        failed_entries += 1
    elif result  is not None:
        total_inventory += int(result)
        new_value = float(input("Enter the delivery amount: "))

        #Process the delivery amount and update the current value 
        current_total = process_delivery(current_total, new_value)

        #add the tax with the delivery amount to the current total
        current_total += calculate_tax(new_value)    
        

        print(f"Total delivery amount: {current_total}")
        print(f"Total quantity: {total_inventory}")
       
        
       
        
       
        
    
    # elif user_input.startswith('-'):
    #     print("Invalid input. Please enter a valid integer number.")
    #     failed_entries += 1
    # #Successful entry  
    # else:
    #     quantity = int(user_input)
    #     total_inventory += quantity

    #     if total_inventory > 500:
    #         print("Overstock Alert: Total inventory exceeds 500 units.")
    #         total_inventory -= quantity  # Revert the addition
    #         break
    #     else:    

    #         print(f"Added {quantity} units. Total inventory is now {total_inventory}.")

5
#Final summary of the audit
# print("\nInventory Audit Summary")
# print("----------------------")
# print(f"Total inventory: {total_inventory} units")
# print(f"Failed entries: {failed_entries}")








"""A dedicated function to print
the final summary """
def generate_report(total_units, failed_attempts):
    return True


