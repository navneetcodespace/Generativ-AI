# Task 1: Discount Rules (if / elif / else)

# Write a program that reads an integer order_amount from the user using input().
order_amount = int(input("Enter Your Order Amount : "))
# Apply the following discount rules and print the final amount:

# order_amount >= 2000 → 15% discount
if (order_amount >= 2000):
    discount = order_amount * (15/100)
    final_Amount = order_amount - discount 
    print(final_Amount)

# 1500 <= order_amount < 2000 → 10% discount

elif (order_amount >= 1500 and order_amount < 2000):
    discount = order_amount * (10/100) 
    final_Amount = order_amount - discount
    print(final_Amount)

# 1000 <= order_amount < 1500 → 7% discount

elif (order_amount >= 1000 and order_amount <1500):
    discount = order_amount * (7/100)
    final_Amount = order_amount - discount
    print (final_Amount)

# otherwise → 0% discount

else : 
    print(order_amount)



# Task 2: Process Multiple Orders (for loop)

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discount_count = 0

for amount in orders:

    if (amount >= 2000):
        discount = amount * (15/100)
        final_Amount = amount - discount
        discount_count += 1
        print(amount, "-> 15% ->", final_Amount)

    elif (amount >= 1500 and amount < 2000):
        discount = amount * (10/100)
        final_Amount = amount - discount
        discount_count += 1
        print(amount, "-> 10% ->", final_Amount)

    elif (amount >= 1000 and amount < 1500):
        discount = amount * (7/100)
        final_Amount = amount - discount
        discount_count += 1
        print(amount, "-> 7% ->", final_Amount)

    else:
        final_Amount = amount
        print(amount, "-> 0% ->", final_Amount)

    total_revenue += final_Amount

print("Total Revenue After Discounts:", total_revenue)
print("Orders with Discount:", discount_count)



# Task 3: User Menu (while loop + break/continue)

orders = []

while True:

    print("\n----- MENU -----")
    print("1 - Add Order Amount")
    print("2 - Show All Orders and Totals")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter Order Amount: "))
        orders.append(amount)

    elif choice == "2":

        total_revenue = 0

        print("\nOrder Amount -> Discount -> Final Amount")

        for amount in orders:

            if amount >= 2000:
                discount = amount * (15 / 100)
                final_amount = amount - discount
                print(amount, "-> 15% ->", final_amount)

            elif amount >= 1500 and amount < 2000:
                discount = amount * (10 / 100)
                final_amount = amount - discount
                print(amount, "-> 10% ->", final_amount)

            elif amount >= 1000 and amount < 1500:
                discount = amount * (7 / 100)
                final_amount = amount - discount
                print(amount, "-> 7% ->", final_amount)

            else:
                final_amount = amount
                print(amount, "-> 0% ->", final_amount)

            total_revenue += final_amount

        print("Total Revenue:", total_revenue)

    elif choice == "q":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice! Try Again.")
        continue




# Task 5: Loop Control with Conditions (break & continue)

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sale in daily:

    if sale == -1:
        print("Corrupted data found. Stopping the program.")
        break

    elif sale == 0:
        print("No sales today.")
        continue

    else:
        total_sales += sale
        print("Running Total:", total_sales)

print("Final Total Sales:", total_sales)