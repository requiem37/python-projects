def most_value(shop):
    best_name = None
    best_price = 0
    for name, price in shop.items():
        if price < 100:
            if price > best_price:
                best_price = price
                best_name = name
    return best_name


