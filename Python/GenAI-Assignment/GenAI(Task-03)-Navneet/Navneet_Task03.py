# Task 1 - Basic Function: Price After Discount

def apply_discount(price, discount_percent = 5):
    if discount_percent > 60:
        discount_percent = 60

    discount = price * (discount_percent/100)
    new_price = price - discount
    
    return new_price


print(apply_discount(1000,10))
print(apply_discount(500))



# Task 2 - Recursive Function: Factorial Utility

def factorial(n):

    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return

    elif n == 0 or n == 1:
        return 1

    else:
        return n * factorial(n - 1)


print(apply_discount(1000, 10))
print(apply_discount(500))
print(apply_discount(1000, 80))



# Task 3 - Lambda Function: GST Calculator

gst = lambda price: price + (0.18 * price)

print(gst(100))



# Task 4 - Using map(): Apply GST to List of Prices

prices = [100, 250, 400, 1200, 50]

gst = lambda price: price + (0.18 * price)

prices_with_gst = list(map(gst, prices))

print("Original Prices:", prices)
print("Prices After GST:", prices_with_gst)



# Task 5 - Using filter()

prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive = list(filter(lambda price: price > 500, prices))

cheap = list(filter(lambda price: price <= 500, prices))

print("Prices Greater Than 500:", expensive)
print("Prices Less Than or Equal to 500:", cheap)


# Task 6 - Combined Utility Function

def process_prices(prices):

    discounted_prices = list(map(lambda price: price - (price * 10 / 100), prices))

    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))

    return discounted_prices, filtered_prices


prices = [100, 250, 400, 1200, 50]

discounted_prices, filtered_prices = process_prices(prices)

print("Discounted Prices:", discounted_prices)
print("Filtered Prices:", filtered_prices)