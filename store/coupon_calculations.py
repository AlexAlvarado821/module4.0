"""
Author: Alex Alvarado
Program: Coupon_Calculations
Date: 9-20-20
Description: calculates the price of a product, taking into consideration a sale, taxes, and coupons.
"""


def calculate_price(price, cash_coupon, percent_coupon):
    with_cashcoupon = price - cash_coupon
    with_percentcoupon = with_cashcoupon - (with_cashcoupon * percent_coupon/100)
    subtotal_tax = with_percentcoupon *1.06
    shipping = 0
    if with_percentcoupon < 10:
        shipping = 5.95
    elif with_percentcoupon < 30:
        shipping = 7.95
    elif with_percentcoupon < 50:
        shipping = 11.95
    else:
        shipping = 0
    return subtotal_tax + shipping


if __name__ == '__main__':
    print(calculate_price(90.50, 10, 10))
    print(calculate_price(85.50, 10, 20))










