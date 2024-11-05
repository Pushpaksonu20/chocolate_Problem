import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("chocolate_house.db")
cursor = conn.cursor()

# Create tables
def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SeasonalFlavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS IngredientInventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CustomerSuggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_suggestion TEXT NOT NULL,
        allergy_concerns TEXT
    )
    ''')
    conn.commit()

# Add a new seasonal flavor
def add_seasonal_flavor(name, description):
    cursor.execute('INSERT INTO SeasonalFlavors (name, description) VALUES (?, ?)', (name, description))
    conn.commit()

# View all seasonal flavors
def view_seasonal_flavors():
    cursor.execute('SELECT * FROM SeasonalFlavors')
    return cursor.fetchall()

# Add an ingredient to inventory
def add_ingredient(ingredient, quantity):
    cursor.execute('INSERT INTO IngredientInventory (ingredient, quantity) VALUES (?, ?)', (ingredient, quantity))
    conn.commit()

# Update ingredient quantity in inventory
def update_ingredient_quantity(ingredient, quantity):
    cursor.execute('UPDATE IngredientInventory SET quantity = ? WHERE ingredient = ?', (quantity, ingredient))
    conn.commit()

# View all ingredients in inventory
def view_inventory():
    cursor.execute('SELECT * FROM IngredientInventory')
    return cursor.fetchall()

# Add a customer flavor suggestion
def add_customer_suggestion(flavor_suggestion, allergy_concerns):
    cursor.execute('INSERT INTO CustomerSuggestions (flavor_suggestion, allergy_concerns) VALUES (?, ?)', (flavor_suggestion, allergy_concerns))
    conn.commit()

# View all customer suggestions
def view_customer_suggestions():
    cursor.execute('SELECT * FROM CustomerSuggestions')
    return cursor.fetchall()

# Menu for the application
def menu():
    print("Welcome to the Chocolate House Management System")
    print("1. Add Seasonal Flavor")
    print("2. View Seasonal Flavors")
    print("3. Add Ingredient to Inventory")
    print("4. Update Ingredient Quantity")
    print("5. View Ingredient Inventory")
    print("6. Add Customer Flavor Suggestion")
    print("7. View Customer Suggestions")
    print("0. Exit")
    
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter flavor name: ")
            description = input("Enter flavor description: ")
            add_seasonal_flavor(name, description)
            print("Flavor added successfully.")
        elif choice == '2':
            flavors = view_seasonal_flavors()
            for flavor in flavors:
                print(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}")
        elif choice == '3':
            ingredient = input("Enter ingredient name: ")
            quantity = int(input("Enter quantity: "))
            add_ingredient(ingredient, quantity)
            print("Ingredient added successfully.")
        elif choice == '4':
            ingredient = input("Enter ingredient name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_ingredient_quantity(ingredient, quantity)
            print("Ingredient quantity updated successfully.")
        elif choice == '5':
            inventory = view_inventory()
            for item in inventory:
                print(f"ID: {item[0]}, Ingredient: {item[1]}, Quantity: {item[2]}")
        elif choice == '6':
            suggestion = input("Enter flavor suggestion: ")
            allergies = input("Enter any allergy concerns: ")
            add_customer_suggestion(suggestion, allergies)
            print("Suggestion added successfully.")
        elif choice == '7':
            suggestions = view_customer_suggestions()
            for suggestion in suggestions:
                print(f"ID: {suggestion[0]}, Flavor Suggestion: {suggestion[1]}, Allergy Concerns: {suggestion[2]}")
        elif choice == '0':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

# Initialize database and tables, then start the menu
create_tables()
menu()

# Close the database connection
conn.close()