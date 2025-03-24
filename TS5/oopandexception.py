# Define the Item class with validation
class Item:
    def __init__(self, item_id, name, description, price):
        if not name.strip():  # Check if the name is empty
            raise ValueError("Item name cannot be empty.")
        if price < 0:  # Ensure the price is not negative
            raise ValueError("Price cannot be negative.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

# Manage items with CRUD operations
class ItemManager:
    def __init__(self):
        self.items = {}  # Store items in a dictionary
        self.next_id = 1  # Auto-increment item ID

    # Create a new item
    def create_item(self, name, description, price):
        try:
            item = Item(self.next_id, name, description, price)
            self.items[self.next_id] = item
            self.next_id += 1
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    # Read and display all items
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(f"ID: {item.id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")

    # Update an existing item
    def update_item(self, item_id, name, description, price):
        if item_id not in self.items:
            print("Item not found.")
            return
        
        try:
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item updated successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    # Delete an item
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found.")

# Sample interaction with the user
def main():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            try:
                price = float(input("Enter item price: "))
                manager.create_item(name, description, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name: ")
                description = input("Enter new description: ")
                price = float(input("Enter new price: "))
                manager.update_item(item_id, name, description, price)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1-5.")

if __name__ == "__main__":
    main()
