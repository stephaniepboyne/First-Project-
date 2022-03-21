def calculate_markup(print):
    difference = print.price % print.printing_cost
    divide = print.printing_cost / difference 
    percent = 100 / divide 
    return percent