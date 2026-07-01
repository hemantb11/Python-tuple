# Hotel Management System using Tuple

# Menu data (tuple inside tuple)
menu=(
    (1, "paneer", 400),
    (2, "chiken", 600),
    (3, "dessert", 200),
    (4, "noodles", 150)
)

# Infinite loop for menu system
while True:
    print("----Hotel Menu Card----\n1.View menu\n2.Order\n3.Generate bill\n4.exit\n")

    # Take user choice
    ch=int(input("enter your choice\n"))

    # Match case for menu options
    match ch:

        # View Menu
        case 1:
            print("Items are:")
            print("------------------------")
            print("ID\tName\tPrice")
            print("------------------------")

            # Display all menu items
            for items in menu:
                print(f"{items[0]}\t{items[1]}\t{items[2]}")

        # Order Item
        case 2:
            item_id = int(input("Enter item id: "))
            qty = int(input("Enter quantity: "))

            # Search item in menu
            for item in menu:
                if item_id == item[0]:

                    # Calculate total price
                    total = item[2] * qty

                    print("Item Name:", item[1])
                    print("Price:", item[2])
                    print("Quantity:", qty)
                    print("Total:", total)
                    break

            else:
                print("Invalid Item ID")

        # Generate Bill
        case 3:
            subtotal = 0

            print("\n--------- BILL ---------")
            print("Item\tQty\tPrice\tAmount")

            # Calculate subtotal
            for i in menu:
                print(f"{i[0]}\t{i[1]}\t{i[2]}")
                subtotal += i[2]

            # GST calculation
            cgst = subtotal * 0.025
            sgst = subtotal * 0.025

            # Final bill
            grand_total = subtotal + cgst + sgst

            print("\n-------------------------")
            print("Subtotal :", subtotal)
            print("CGST 2.5% :", cgst)
            print("SGST 2.5% :", sgst)
            print("-------------------------")
            print("Grand Total :", grand_total)

        # Exit Program
        case 4:
            print("Thank you! Visit Again!")
            break

        # Invalid choice handling
        case _:
            print("Invalid Choice")