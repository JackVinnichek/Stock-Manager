"""1. Project Overview
You are tasked with building a high-performance inventory management system (Tracking: Stock, Library Books, or Game Loot). The system must not only store and retrieve data but also analyze historical usage to provide predictive insights regarding future stock levels.

2. Technical Constraints
Regardless of your chosen language (Java or Python), your project must meet the following architectural standards:

A. Dynamic Data Management
No Fixed Arrays: You must manage your collection using a dynamic structure.


Python: Use Lists or Dictionaries, but demonstrate manual manipulation (no over-reliance on external libraries like Pandas).

Search & Sort: You must implement a Binary Search for item lookups. This requires your collection to be sorted. You must implement a recursive sorting algorithm (Merge Sort or Quick Sort) to maintain this order.  # you will have to research this!

B. Predictive Logic (The "Smart" Component)
Your system must calculate a Burn Rate for every item to forecast depletion.

Formula: Develop a formula that will calculate the items per time period

Predictive Output: For any searched item, the system must display the estimated days remaining before the quantity hits zero.

Edge Case Handling: You must programmatically handle items with zero usage (Burn Rate = 0) to avoid "Division by Zero" errors.

C. File I/O & Persistence
Lifecycle: The program must check for an existing data file (.csv, .json, or .txt) on startup.

Save on Exit: Any changes made during the session must be persisted back to the file.

Data Integrity: Use try-catch (Java) or try-except (Python) blocks to handle missing or corrupted files without the program crashing.

3. Architecture Requirements (Choose One Path)

The Python Path (Focus: Efficiency & Clarity)
Type Hinting: Use the typing module to define function signatures.  # you will have to research this!

Decorators: Use @property for attribute access. # you will have to research this!

List Comprehensions: Use Pythonic idioms for filtering and searching through the inventory."""
import json
from typing import List
class InventoryItem:
    def __init__(self, name: str, quantity: int, usage_history: List[int]):
        self.name = name
        self.quantity = quantity
        self.usage_history = usage_history

    @property
    def burn_rate(self) -> float:
        if not self.usage_history:
            return 0.0
        return sum(self.usage_history) / len(self.usage_history)

    def predict_depletion(self) -> str:
        if self.burn_rate == 0:
            return "No usage history available."
        days_remaining = self.quantity / self.burn_rate
        return f"Estimated days remaining: {days_remaining:.2f}"
class InventoryManager: 
    # display all inventory items with quantity, burn rate, and predicted depletion

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.inventory: List[InventoryItem] = []
        self.load_inventory()
    # load inventory data from a JSON file and handle missing or corrupted files
    def load_inventory(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)

                for item in data:
                    self.inventory.append(
                        InventoryItem(
                            name=item['name'],
                            quantity=item['quantity'],
                            usage_history=item['usage_history']
                    )
                )
            self.inventory = self.merge_sort(self.inventory)
        except FileNotFoundError:
            print("No existing inventory file found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print("Inventory file is corrupted. Starting with an empty inventory.")
    # save inventory data to a JSON file with error handling1

    def save_inventory(self):
        with open(self.file_path, 'w') as file:
            json.dump([{
                'name': item.name,
                'quantity': item.quantity,
                'usage_history': item.usage_history
            } for item in self.inventory], file)

    def add_item(self, name: str, quantity: int, usage_history: List[int]):
        self.inventory.append(InventoryItem(name, quantity, usage_history))
        # recursive merge sort that sorts inventory items alphabetically by item name
        # sort inventory using merge sort after adding a new item

        self.inventory = self.merge_sort(self.inventory)
        
    def merge_sort(self, items: List[InventoryItem]) -> List[InventoryItem]:
        if len(items) <= 1:
            return items
        mid = len(items) // 2
        left_half = self.merge_sort(items[:mid])
        right_half = self.merge_sort(items[mid:])
        return self.merge(left_half, right_half)
    def merge(self, left: List[InventoryItem], right: List[InventoryItem]) -> List[InventoryItem]:
        sorted_items = []
        while left and right:
            if left[0].name < right[0].name:
                sorted_items.append(left.pop(0))
            else:
                sorted_items.append(right.pop(0))
        sorted_items.extend(left)
        sorted_items.extend(right)
        return sorted_items
    

    def search_item(self, name: str) -> str:
        # binary search function that searches for an inventory item by name in a sorted list
        left, right = 0, len(self.inventory) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.inventory[mid].name == name:
                return f"Item: {self.inventory[mid].name}, Quantity: {self.inventory[mid].quantity}, Burn Rate: {self.inventory[mid].burn_rate:.2f}, {self.inventory[mid].predict_depletion()}"
            elif self.inventory[mid].name < name:
                left = mid + 1
            else:
                right = mid - 1
        return "Item not found in inventory."
    
if __name__ == "__main__":
    # create a menu system for adding items, searching items, displaying inventory, and saving data
    manager = InventoryManager('inventory.json')
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Search Item")
        print("3. Display Inventory")
        print("4. Save and Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            usage_history = list(map(int, input("Enter usage history (comma separated): ").split(',')))
            manager.add_item(name, quantity, usage_history)
        elif choice == '2':
            name = input("Enter item name to search: ")
            print(manager.search_item(name))
        elif choice == '3':
            for item in manager.inventory:
                print(f"Item: {item.name}, Quantity: {item.quantity}, Burn Rate: {item.burn_rate:.2f}, {item.predict_depletion()}")
        elif choice == '4':
            manager.save_inventory()
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")