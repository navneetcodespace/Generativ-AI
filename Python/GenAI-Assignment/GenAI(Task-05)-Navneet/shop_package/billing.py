def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    return total

def apply_tax(amount):
    tax = amount * (5/100)
    final_amount = amount + tax

    return final_amount

