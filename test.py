def calculate_markup(price, printing_cost):
    division = price / printing_cost
    percent = division * 100
    markup = percent - 100
    return markup

print(calculate_markup(40, 25))
