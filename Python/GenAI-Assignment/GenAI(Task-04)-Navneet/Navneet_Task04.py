# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt","w") as file:
    for sale in sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    print(file.read())


# Task 2

# Read entire file
with open("sales_data.txt", "r") as file:
    print(file.read())

# Read first line
with open("sales_data.txt", "r") as file:
    print(file.readline())

# Read all lines and convert to integers
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = []

for line in lines:
    sales.append(int(line.strip()))

print(sales)


# Task 3

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")

with open("sales_data.txt", "r") as file:
    print(file.read())

# Extra (Optional)

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

print("Total Lines:", len(lines))


# Task 4

with open("sales_data.txt", "r") as file:
    lines = file.readlines()

sales = []

for line in lines:
    sales.append(int(line.strip()))

total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)

# Extra (Optional)

count = 0

for sale in sales:
    if sale > average_sale:
        count += 1

print("Sales Above Average:", count)