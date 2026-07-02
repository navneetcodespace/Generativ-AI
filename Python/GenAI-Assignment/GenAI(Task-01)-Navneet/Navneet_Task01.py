# Task 1: Product Collections (Lists & Tuples)

# Create a list named products containing at least 6 product names (strings).
product_list = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]

# Create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product = ("Laptop", 999.99, "Electronics")

# Print the 2nd and last product from the products list
print("2nd product:", product_list[1])
print("Last product:", product_list[-1])

# Append two new product names to products and then print the updated list.
product_list.append("Tablet")
product_list.append("Smartwatch")
print("Updated product list:", product_list)



# Task 2: Categories (Sets)

# From your products list, create a set of categories called categories_set. (If product names do not contain categories, create a short parallel list categories = [...] with matching length and use that.)
categories = ["Electronics", "Accessories", "Computers", "Electronics", "Accessories", "Computers"]
categories_set = set(categories)

# Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Cameras")
categories_set.add("Electronics") 
print("Categories set after adding new categories:", categories_set)


# Show how to check whether a category exists in the set (print a boolean result).
category_to_check = "Electronics"
print(category_to_check in categories_set)


# Task 3: Product Pricing (Dictionaries)

# Create a dictionary price_dict where keys are product names and values are prices (integers or floats). Include at least 6 entries.
price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 199.99,
    "Monitor": 299.99,
    "Keyboard": 49.99,
    "Mouse": 29.99,
}

# Write small code blocks to:

# Add a new product with price to price_dict.
price_dict["Tablet"] = 399.99
print(price_dict)

# Update the price of an existing product.
price_dict["Smartphone"] = 899.99
print(price_dict)

# Remove a product by name (handle the case when the product does not exist).
if "Tablet" in price_dict:
    del price_dict["Tablet"]

print(price_dict)

# Print the average price of all products (use only dictionary operations and basic arithmetic).

average = sum(price_dict.values()) / len(price_dict)
print(average)

# Task 4: Combined Operations

# Using the products list and price_dict, create a list of tuples named catalog where each tuple is:
# (product_name, price, category)
product_list = ["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard", "Mouse"]

price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 199.99,
    "Monitor": 299.99,
    "Keyboard": 49.99,
    "Mouse": 29.99,
}

categories = ["Electronics", "Accessories", "Computers", "Electronics", "Accessories", "Computers"]

catalog = [ ]

for i in range(len(product_list)):
    product = product_list[i]
    price = price_dict[product]
    category = categories[i]

    catalog.append((product, price, category))

print(catalog)

# From catalog, create a new dictionary category_to_products that maps each category to a list of product names in that category.
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)

# Print all products that belong to the category that has the maximum number of products.
max_category = ""
max_count = 0
 
 
for category in category_to_products:
    if len(category_to_products[category]) > max_count:
        max_count = len(category_to_products[category])
        max_category = category

print("Category:", max_category)
print("Products:")

for product in category_to_products[max_category]:
    print(product)