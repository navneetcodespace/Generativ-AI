def apply_discount(price,percent):
    discount = price * (percent/100)
    final_price = price - discount

    return final_price


def flat_discount(price):
    discount = price * (50/100)
    final_price = price - discount

    return final_price