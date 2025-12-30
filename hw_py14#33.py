from prettytable import PrettyTable

"""
INTERACTIVE INVENTORY MANAGEMENT SYSTEM - STUDENT PROJECT
========================================================

PROJECT OVERVIEW:
Create an interactive inventory management system that allows users to manage 
a collection of items. Students will implement various functions to manipulate 
inventory data and create a user-friendly interface.

BASE INVENTORY DATA:
Start with the provided dictionary as your base inventory with 8 pre-loaded items
across different categories (Electronics, Office, Kitchen, Furniture).

REQUIRED FUNCTIONS:

1. display_inventory(inventory)
   - Purpose: Show all items in a formatted table
   - Parameters: inventory (dictionary)
   - Returns: Nothing (prints to console)
   - Features: Display item name, quantity, price, category in columns
     Calculate and show total inventory value
     Handle empty inventory gracefully

2. add_item_to_inventory(inventory, item_name, quantity, price, category)
   - Purpose: Add new items or update existing ones
   - Parameters: inventory, item_name, quantity, price, category
   - Returns: Updated inventory dictionary
   - Logic: If item exists, add to existing quantity
     If item is new, create new entry
     Provide user feedback about the action

3. remove_item_from_inventory(inventory, item_name, quantity)
   - Purpose: Remove items from inventory
   - Parameters: inventory, item_name, quantity
   - Returns: Updated inventory dictionary
   - Logic: Check if item exists, verify sufficient quantity
     Remove items and delete entry if quantity becomes 0
     Provide appropriate error messages

4. search_inventory(inventory, search_term)
   - Purpose: Find items by name or category
   - Parameters: inventory, search_term
   - Returns: Nothing (prints results to console)
   - Features: Search in both item names and categories
     Case-insensitive search, display matching items

5. get_category_summary(inventory)
   - Purpose: Show inventory statistics by category
   - Parameters: inventory
   - Returns: Nothing (prints summary to console)
   - Features: Group items by category, count total items per category
     Calculate total value per category

6. show_menu()
   - Purpose: Display the main menu options
   - Parameters: None
   - Returns: Nothing (prints menu to console)
   - Menu Options: 1-View Inventory, 2-Add Item, 3-Remove Item
     4-Search Items, 5-Category Summary, 6-Exit

7. main()
   - Purpose: Run the interactive program loop
   - Parameters: None
   - Returns: Nothing
   - Features: Initialize base inventory, display welcome message
     Run continuous menu loop, handle user input
     Provide input validation, show final inventory before exiting

PROGRAM FLOW REQUIREMENTS:
1. Start: Display welcome message and show base inventory has 8 items
2. Menu Loop: Continuously show menu and get user choice
3. Input Validation: Check for valid menu choices and data types
4. User Feedback: Provide clear messages for all actions (success/error)
5. Error Handling: Gracefully handle invalid inputs and edge cases
6. Exit: Show final inventory status before closing

TECHNICAL REQUIREMENTS:
- Functions: Must use all 7 required functions
- Parameters: Functions should accept appropriate parameters
- Return Values: Functions should return meaningful values when needed
- Default Parameters: Use default parameters where appropriate
- Docstrings: Include proper documentation for each function
- Input Validation: Check user inputs for validity
- User Experience: Clear prompts and feedback messages

TESTING SCENARIOS:
- Add a new item (e.g., "Wireless Keyboard" at $45.99 in "Electronics")
- Remove items from existing inventory
- Search for items by name or category
- View category summaries
- Handle invalid inputs gracefully
- Exit and see final inventory status

LEARNING OBJECTIVES:
- Function Design: Creating functions with appropriate parameters and return values
- Data Manipulation: Working with nested dictionaries and lists
- User Input: Handling various types of user input safely
- Error Handling: Managing edge cases and invalid inputs
- Program Flow: Creating interactive loops and menus
- Data Validation: Ensuring data integrity and user experience

BONUS CHALLENGES:
- Add inventory export/import functionality
- Implement low stock warnings
- Add item modification (change price/category)
- Create inventory reports with date stamps
- Add sorting options (by name, price, category)
"""


def display_inventory(inventory):
    """
    Display the current inventory in a formatted way.
    """
    if not inventory:
        print("Inventory is empty.\n")
        return

    print(f"{'Item Name':<20} {'Quantity':<10} {'Price':<10} {'Category':<15}")
    print("-" * 60)
    total_value = 0
    for item, info in inventory.items():
        print(f"{item:<20} {info['quantity']:<10} ${info['price']:<9.2f} {info['category']:<15}")
        total_value += info['quantity'] * info['price']
    print("-" * 60)
    print(f"Total Inventory Value: ${total_value:.2f}\n")


def add_item_to_inventory(inventory, item_name, quantity, price, category):
    """
    Add a new item or update existing item in inventory.
    """
    if item_name in inventory:
        inventory[item_name]['quantity'] += quantity
        print(f"Updated {item_name}, new quantity: {inventory[item_name]['quantity']}")
    else:
        inventory[item_name] = {'quantity': quantity, 'price': price, 'category': category}
        print(f"Added new item: {item_name}")
    return inventory


def remove_item_from_inventory(inventory, item_name, quantity):
    """
    Remove items from inventory.
    """
    if item_name not in inventory:
        print(f"Error: {item_name} does not exist in inventory.")
        return inventory

    if quantity > inventory[item_name]['quantity']:
        print(f"Error: Not enough quantity of {item_name} to remove.")
        return inventory

    inventory[item_name]['quantity'] -= quantity
    print(f"Removed {quantity} of {item_name}. Remaining: {inventory[item_name]['quantity']}")

    if inventory[item_name]['quantity'] == 0:
        del inventory[item_name]
        print(f"{item_name} has been completely removed from inventory.")
    return inventory


def search_inventory(inventory, search_term):
    """
    Search for items in inventory by name or category.
    """
    search_term = search_term.lower()
    results = {}
    for item, info in inventory.items():
        if search_term in item.lower() or search_term in info['category'].lower():
            results[item] = info

    if not results:
        print(f"No items found matching '{search_term}'.\n")
    else:
        display_inventory(results)


def get_category_summary(inventory):
    """
    Show summary of inventory by category.
    """
    from collections import defaultdict

    category_data = defaultdict(lambda: {'count': 0, 'value': 0})
    for item, info in inventory.items():
        cat = info['category']
        category_data[cat]['count'] += info['quantity']
        category_data[cat]['value'] += info['quantity'] * info['price']

    print(f"{'Category':<15} {'Total Items':<12} {'Total Value':<12}")
    print("-" * 40)
    for cat, data in category_data.items():
        print(f"{cat:<15} {data['count']:<12} ${data['value']:<.2f}")
    print()


def show_menu():
    """
    Display the main menu options.
    """
    print("Inventory Management System")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Search Items")
    print("5. Category Summary")
    print("6. Exit")


def main():
    """
    Main function to run the interactive inventory system.
    """
    base_inventory = {
        "Laptop": {"quantity": 5, "price": 999.99, "category": "Electronics"},
        "Mouse": {"quantity": 15, "price": 25.50, "category": "Electronics"},
        "Notebook": {"quantity": 50, "price": 5.99, "category": "Office"},
        "Pen": {"quantity": 100, "price": 1.99, "category": "Office"},
        "Coffee Mug": {"quantity": 20, "price": 12.99, "category": "Kitchen"},
        "Desk Lamp": {"quantity": 8, "price": 45.00, "category": "Furniture"},
        "USB Cable": {"quantity": 25, "price": 8.99, "category": "Electronics"},
        "Paper Clips": {"quantity": 200, "price": 0.99, "category": "Office"}
    }

    inventory = base_inventory.copy()
    print("Welcome to the Interactive Inventory Management System!\n")
    display_inventory(inventory)

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        print()

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            try:
                name = input("Item Name: ").strip()
                qty = int(input("Quantity: "))
                price = float(input("Price: "))
                category = input("Category: ").strip()
                inventory = add_item_to_inventory(inventory, name, qty, price, category)
            except ValueError:
                print("Invalid input. Quantity must be integer and price must be numeric.\n")
        elif choice == '3':
            try:
                name = input("Item Name to remove: ").strip()
                qty = int(input("Quantity to remove: "))
                inventory = remove_item_from_inventory(inventory, name, qty)
            except ValueError:
                print("Invalid input. Quantity must be integer.\n")
        elif choice == '4':
            term = input("Enter name or category to search: ").strip()
            search_inventory(inventory, term)
        elif choice == '5':
            get_category_summary(inventory)
        elif choice == '6':
            print("Final inventory status:\n")
            display_inventory(inventory)
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.\n")


if __name__ == "__main__":
    main()