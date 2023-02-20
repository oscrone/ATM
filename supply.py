import tkinter as tk
from tkinter import ttk
import ast


class MoneySupply:
    def __init__(self):
        self.supply = {}  # a dict that contains bills: 10, 20, 50, 100, 200; and their qty
        self.load_supply_file()

    def load_supply_file(self):
        try:
            f = open("bills/supply.txt", "r")
            self.supply = ast.literal_eval(f.read())
            print("Supply info loaded.")
        except ValueError:
            print("there was an error while loading supply info")
        finally:
            f.close()

    def save_supply_file(self):
        try:
            f = open("bills/supply.txt", "w")
            f.write(str(self.supply))
            print("Supply file saved.")
        except ValueError:
            print("there was an error while saving supply info")
        finally:
            f.close()

    def supply_check(self, amount):
        check_amount = amount
        bill_collector = self.supply.copy()
        missing_bill = self.supply.copy()
        [missing_bill.update({x: False}) for x in missing_bill]
        [bill_collector.update({x: 0}) for x in bill_collector]
        for x in reversed(self.supply):
            while x <= check_amount:
                if self.supply[x] > 0:
                    bill_collector[x] += 1
                    self.supply[x] -= 1
                    print(f"issued: {x}")
                    check_amount -= x
                else:
                    missing_bill[x] = True
                    print(f"missing bill: {x}")
                    break
        if check_amount != 0:
            message = "ATM Machine doesn't have enough bills to print Your request.\nMissing bills:\n"
            for x in missing_bill:
                if missing_bill[x]:
                    message += f"\n{x}$ Bill\n"
                self.supply[x] += bill_collector[x]
            self.supply_warning(message)
            self.bills_left()
            return False
        else:
            self.save_supply_file()
            self.bills_left()
            return True

    def bills_left(self):
        [print(f"{x}$ bills left: {self.supply[x]}") for x in self.supply]
        total = 0
        for x in self.supply:
            total += x * self.supply[x]
        print(f"Total ATM cash: {total}$")

    def supply_warning(self, message):
        warning_win = tk.Tk()
        warning_win.title("Supply Warning")
        warning_frame = ttk.Frame(warning_win, padding=40)
        warning_frame.grid()
        ttk.Label(warning_frame, text=message, justify="center").grid()
        ttk.Button(warning_frame, text="Ok", command=warning_win.destroy).grid()