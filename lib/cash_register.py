#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.previous_total = 0
        self.items = []

    def add_item(self, title, price, quantity = 1):
        self.previous_total = price * quantity
        self.total += self.previous_total
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:    
            discount_perc = (100 - float(self.discount)) / 100
            self.total = int(self.total * discount_perc)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        self.total -= self.previous_total
