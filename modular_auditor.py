#Initialize variables to keep track of total inventory and failed entries
total_inventory = 0
failed_entries = 0


print("Inventory Audit System")
print("----------------------")

while True:
    user_input = input("Enter item name and quantity (or type 'quit' to finish): ").strip()

    if user_input.lower() == 'quit':
        break
    #Validation for user input
    elif not user_input.isdigit():
        print("Invalid input. Please enter a valid integer number.")
        failed_entries += 1
    elif user_input.startswith('-'):
        print("Invalid input. Please enter a valid integer number.")
        failed_entries += 1
    #Successful entry  
    else:
        quantity = int(user_input)
        total_inventory += quantity

        if total_inventory > 500:
            print("Overstock Alert: Total inventory exceeds 500 units.")
            total_inventory -= quantity  # Revert the addition
            break
        else:    
            print(f"Added {quantity} units. Total inventory is now {total_inventory}.")

#Final summary of the audit
print("\nInventory Audit Summary")
print("----------------------")
print(f"Total inventory: {total_inventory} units")
print(f"Failed entries: {failed_entries}")