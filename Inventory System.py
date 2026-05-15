import json
import os


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"{self.product_id} | {self.name} | {self.price} | {self.quantity}")

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }


class Inventory:
    def __init__(self):
        self.products = []
        self.file = "inventory.json"
        self.load_data()

    # LOAD DATA
    def load_data(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                data = json.load(f)
                for item in data:
                    p = Product(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["quantity"]
                    )
                    self.products.append(p)

    # SAVE DATA
    def save_data(self):
        data = []
        for p in self.products:
            data.append(p.to_dict())

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    # ADD PRODUCT
    def add_product(self):
        pid = input("Enter ID: ")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))

        p = Product(pid, name, price, qty)
        self.products.append(p)
        self.save_data()
        print("Product added successfully!")

    # VIEW PRODUCTS
    def view_products(self):
        if not self.products:
            print("No products found.")
            return

        print("\n--- INVENTORY ---")
        for p in self.products:
            p.display()

    # SEARCH
    def search_product(self):
        pid = input("Enter ID to search: ")

        for p in self.products:
            if p.product_id == pid:
                print("Product found:")
                p.display()
                return

        print("Product not found.")

    # DELETE
    def delete_product(self):
        pid = input("Enter ID to delete: ")

        for p in self.products:
            if p.product_id == pid:
                self.products.remove(p)
                self.save_data()
                print("Product deleted.")
                return

        print("Product not found.")

    # UPDATE
    def update_product(self):
        pid = input("Enter ID to update: ")

        for p in self.products:
            if p.product_id == pid:
                print("1. Update Price")
                print("2. Update Quantity")
                choice = input("Choose: ")

                if choice == "1":
                    p.price = float(input("New price: "))
                elif choice == "2":
                    p.quantity = int(input("New quantity: "))
                else:
                    print("Invalid choice")
                    return

                self.save_data()
                print("Product updated.")
                return

        print("Product not found.")

    # LOW STOCK
    def low_stock(self):
        print("\nLow stock products (qty < 5):")
        found = False

        for p in self.products:
            if p.quantity < 5:
                p.display()
                found = True

        if not found:
            print("No low stock items.")

    # TOTAL VALUE
    def total_value(self):
        total = 0

        for p in self.products:
            total += p.price * p.quantity

        print("Total Inventory Value:", total)


# ---------------- MAIN PROGRAM ----------------
inv = Inventory()
while True:
    print("\n===== INVENTORY SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Update Product")
    print("6. Low Stock Alert")
    print("7. Total Value")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        inv.add_product()
    elif choice == "2":
        inv.view_products()
    elif choice == "3":
        inv.search_product()
    elif choice == "4":
        inv.delete_product()
    elif choice == "5":
        inv.update_product()
    elif choice == "6":
        inv.low_stock()
    elif choice == "7":
        inv.total_value()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")