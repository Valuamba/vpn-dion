

one_month_price = 290


def calculate_discount(list_price, selling_price):
    discount = ((list_price - selling_price) / list_price) * 100
    return round(discount)


six_month_price = 890
six_month_discount = calculate_discount((6 * 290), six_month_price)


twelve_month_price=1490
twelve_month_discount = calculate_discount((12 * 290), twelve_month_price)


# def caclulate_total(month =):


disc_result_1 = 12 * one_month_price * 10 * (100-twelve_month_discount) / 100

disc_result_2 = twelve_month_price * 10

pass