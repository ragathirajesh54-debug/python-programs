# ==========================================
# SHOP MANAGEMENT SYSTEM
# School Project – Python
# ==========================================

import os
from datetime import datetime

PRODUCT_FILE = "products.txt"
SALES_FILE = "sales.txt"

# ---------- Load Products ----------
def load_products():
    products = []
    if os.path.exists(PRODUCT_FILE):
        with open(PRODUCT_FILE, "r") as file:
            for line in file:
                pid, name, price, qty = line.strip().split(",")
                products.append({
                    "id": int(pid),
                    "name": name,
                    "price": float(price),
                    "qty": int(qty)
                })
    return products


# ---------- Save Products ----------
def save_products(products):
    with open(PRODUCT_FILE, "w") as file:
        for p in products:
            file.write(f"{p['id']},{p['name']},{p['price']},{p['qty']}\n")


# ---------- Add Product ----------
def add_product(products):
    print("\nADD PRODUCT")
    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))

    products.append({
        "id": pid,
        "name": name,
        "price": price,
        "qty": qty
    })

    save_products(products)
    print("Product Added Successfully")


# ---------- View Products ----------
def view_products(products):
    print("\nPRODUCT LIST")
    print("ID\tName\t\tPrice\tQuantity")
    print("--------------------------------------")

    if not products:
        print("No products available")
        return

    for p in products:
        print(f"{p['id']}\t{p['name']}\t{p['price']}\t{p['qty']}")


# ---------- Update Product ----------
def update_product(products):
    pid = int(input("Enter Product ID to Update: "))

    for p in products:
        if p["id"] == pid:
            p["name"] = input("Enter New Name: ")
            p["price"] = float(input("Enter New Price: "))
            p["qty"] = int(input("Enter New Quantity: "))
            save_products(products)
            print("Product Updated Successfully")
            return

    print("Product Not Found")


# ---------- Delete Product ----------
def delete_product(products):
    pid = int(input("Enter Product ID to Delete: "))

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            save_products(products)
            print("Product Deleted Successfully")
            return

    print("Product Not Found")


# ---------- Billing ----------
def generate_bill(products):
    cart = []
    total = 0

    print("\nBILLING SYSTEM")
    while True:
        pid = int(input("Enter Product ID (0 to finish): "))
        if pid == 0:
            break

        for p in products:
            if p["id"] == pid:
                qty = int(input("Enter Quantity: "))
                if qty <= p["qty"]:
                    amount = qty * p["price"]
                    p["qty"] -= qty
                    total += amount
                    cart.append((p["name"], qty, amount))
                else:
                    print("Not enough stock")
                break
        else:
            print("Product not found")

    save_products(products)
    save_sales(cart, total)

    print("\n----- BILL -----")
    for item in cart:
        print(f"{item[0]} x {item[1]} = Rs.{item[2]}")
    print("----------------")
    print("TOTAL AMOUNT = Rs.", total)
    print("Thank You! Visit Again")


# ---------- Save Sales ----------
def save_sales(cart, total):
    with open(SALES_FILE, "a") as file:
        file.write("\n" + str(datetime.now()) + "\n")
        for item in cart:
            file.write(f"{item[0]} x {item[1]} = {item[2]}\n")
        file.write(f"Total = {total}\n")


# ---------- Main Menu ----------
def main():
    products = load_products()

    while True:
        print("\n====== SHOP MANAGEMENT SYSTEM ======")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Generate Bill")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6): ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            view_products(products)
        elif choice == "3":
            update_product(products)
        elif choice == "4":
            delete_product(products)
        elif choice == "5":
            generate_bill(products)
        elif choice == "6":
            print("Exiting Program")
            break
        else:
            print("Invalid Choice")


# ---------- Program Start ----------
main()
