from abc import ABC, abstractmethod

class InventoryItem(ABC):
    i_list = []
    categories = set()
    dictt = {}

    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    @abstractmethod
    def add(self):
        pass

    @classmethod
    def remove(cls, item_name):
        if item_name in cls.dictt:
            removed_item = cls.dictt.pop(item_name)
            cls.i_list = [item for item in cls.i_list if item.name != item_name]
            cls.categories = {item.category for item in cls.i_list}
            print(f"{item_name} removed.")
        else:
            print(f"{item_name} not found.")

    def update(self):
        try:
            updt = input("Enter the item name for updation: ")

            if updt not in InventoryItem.dictt:
                print(f"{updt} is not found.")
                return

            print(f"Current details of {updt}: {InventoryItem.dictt[updt]}")

            field_to_update = input(
                "Enter the field to update (price, quantity, category): "
            ).lower()

            if field_to_update not in ["price", "quantity", "category"]:
                print(
                    "Invalid field. Please enter 'price', 'quantity', or 'category'."
                )
                return

            new_value = input(f"Enter the new value for {field_to_update}: ")

            try:
                new_value = (
                    float(new_value) if field_to_update == "price" else int(new_value)
                )
            except ValueError:
                print(
                    "Invalid input. Please enter a valid value for the chosen field."
                )
                return

            InventoryItem.dictt[updt][field_to_update] = new_value
            for item in InventoryItem.i_list:
                if item.name == updt:
                    setattr(item, field_to_update, new_value)

            print(f"{updt} updated successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid value for the chosen field.")

    @classmethod
    def view_inventory(cls):
        print("Current Inventory:")
        for item in cls.i_list:
            print(
                f"Name: {item.name}, Price: {item.price}, Quantity: {item.quantity}, Category: {item.category}"
            )

    @classmethod
    def low_stock_report(cls):
        low_stock_items = [item for item in cls.i_list if item.quantity < 10]
        if low_stock_items:
            print("Low Stock Report:")
            for item in low_stock_items:
                print(
                    f"Name: {item.name}, Quantity: {item.quantity} (Low Stock!)"
                )
        else:
            print("No items are low in stock.")

class Electronics(InventoryItem):
    def __init__(self, name, price, quantity, category, model):
        super().__init__(name, price, quantity, category)
        self.model = model

    def add(self):
        try:
            i_name = input("Enter the name of the item: ")
            i_price = float(input("Enter the price of the item: "))
            i_quantity = int(input("Enter the number of items: "))
            i_category = input("Enter Item Description: ")

            if i_price > 0 and i_quantity > 0:
                self.quantity = i_quantity
                self.price = i_price
            else:
                print(f"{i_price} and {i_quantity} are not valid inputs.")
                return None

            e_model = input("Enter the model of item: ")
            self.model = e_model

            item = Electronics(i_name, self.price, i_quantity, i_category, self.model)
            InventoryItem.i_list.append(item)
            InventoryItem.categories.add(i_category)
            InventoryItem.dictt[i_name] = {
                "price": self.price,
                "quantity": self.quantity,
                "category": i_category,
                "model": self.model,
            }

            return item

        except ValueError:
            print("Enter the PRICE and QUANTITY in numbers.")
            return None

while True:
    print("\nInventory Management System Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View Inventory")
    print("5. Low Stock Report")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        item = Electronics("", 0, 0, "", "")  # Initialize with default values
        item.add()
    elif choice == "2":
        item_name = input("Enter the name of the item to remove: ")
        InventoryItem.remove(item_name)
    elif choice == "3":
        item = InventoryItem()
        item.update()
    elif choice == "4":
        InventoryItem.view_inventory()
    elif choice == "5":
        InventoryItem.low_stock_report()
    elif choice == "6":
        print("Exiting the Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
