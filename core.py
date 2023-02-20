import time
import tkinter as tk
from tkinter import ttk
from user import User
from supply import MoneySupply


if __name__ == '__main__':
    print('Main program initializing...')


def clear_previous(frame):
    try:
        if not frame:
            pass
        else:
            frame.grid_forget()
    except EOFError:
        print("error while clearing page")


class WelcomeScreen:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="Welcome to the JoJo™\nATM Machine.\n",
                                justify="center")
        self.button1 = ttk.Button(self.frame, text="Proceed to choose credit card.",
                                  command=lambda: choose_card.init_frame(self.frame))

    def init_frame(self, frame):
        clear_previous(frame)
        self.frame.grid()
        self.label1.grid()
        self.button1.grid()
        print("▶ Welcome Screen ◀")


class ChooseCard:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="Pick one of the credit cards to put into the machine:")
        self.image1 = tk.PhotoImage(file="images/credit1.png").subsample(3)
        self.image2 = tk.PhotoImage(file="images/credit2.png").subsample(3)
        self.image3 = tk.PhotoImage(file="images/credit3.png").subsample(3)
        self.button1 = ttk.Button(self.frame, image=self.image1, command=lambda: self.toss(622844))
        self.button2 = ttk.Button(self.frame, image=self.image2, command=lambda: self.toss(999666))
        self.button3 = ttk.Button(self.frame, image=self.image3, command=lambda: self.toss(120120))
        self.button4 = ttk.Button(self.frame, text="Go Back", command=lambda: welcome_screen.init_frame(self.frame))

    def toss(self, id):             # just a small function to tidy up the buttons
        loading_page.init_frame(self.frame, id)

    def init_frame(self, frame):
        clear_previous(frame)
        self.frame.grid()
        self.label1.grid(row=0, column=1)
        self.button1.grid(row=1, column=0)
        self.button2.grid(row=1, column=1)
        self.button3.grid(row=1, column=2)
        self.button4.grid(row=2, column=1)
        print("▶ Identity Screen ◀")


class LoadingPage:
    def __init__(self, win):
        self.tk_window = win
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="Authenticating credentials...")
        self.loading_label = ttk.Label(self.frame, text="▯" * 50)
        self.percentage_label = ttk.Label(self.frame, text="0%")

    def init_frame(self, frame, id):
        clear_previous(frame)
        print("▶ Loading Screen ◀")
        self.frame.grid()
        self.label1.grid()
        self.loading_label.grid()
        self.percentage_label.grid()
        self.progress_bar()
        user_data.authenticate(id)
        time.sleep(1)
        account_menu.init_frame(self.frame)

    def progress_bar(self):
        print("Loading...")
        l = 0
        u = 50
        for x in range(51):
            self.loading_label.config(text=("▮" * l) + ("▯" * u))
            self.percentage_label.config(text=str(l * 2) + "%")
            self.tk_window.update()
            time.sleep(0.035)
            l += 1
            u -= 1


class AccountMenu:
    def __init__(s, win):
        s.frame = ttk.Frame(win, padding=180)
        s.move_type = ""
        s.label1 = ttk.Label(s.frame, text=f"Welcome Dupa\nChoose option:", justify="center")
        s.button1 = ttk.Button(s.frame, text="Withdrawal", command=lambda: s.movement_choice("withdraw", s.frame))
        s.button2 = ttk.Button(s.frame, text="Deposit", command=lambda: s.movement_choice("deposit", s.frame))
        s.button3 = ttk.Button(s.frame, text="Check Balance", command=lambda: check_screen.init_frame(s.frame))
        s.button4 = ttk.Button(s.frame, text="Log Off", command=lambda: welcome_screen.init_frame(s.frame))

    def movement_choice(self, choice, frame):
        self.move_type = choice
        template_picker.init_frame(frame)

    def init_frame(self, frame):
        clear_previous(frame)
        self.frame.grid()
        self.label1.grid()
        self.label1.config(text=f"Welcome {user_data.userdata[1]}\nChoose option:")
        self.button1.grid()
        self.button2.grid()
        self.button3.grid()
        self.button4.grid()
        print("▶ Account Menu Screen ◀")


class CheckScreen:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="Dup", justify="center")
        self.button1 = ttk.Button(self.frame, text="Go Back", command=lambda: account_menu.init_frame(self.frame))

    def init_frame(self, frame):
        clear_previous(frame)
        text = f"Account holder {user_data.userdata[1]}.\n\n" \
               f"Your current account balance is:\n\n{user_data.userdata[2]}$\n"
        self.label1.config(text=text)
        self.frame.grid()
        self.label1.grid()
        self.button1.grid()
        print("▶ Balance Screen ◀")


class TemplatePicker:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="Dup")
        self.button1 = ttk.Button(self.frame, text="50", command=lambda: confirm_save_window.checker(50, self.frame))
        self.button2 = ttk.Button(self.frame, text="100", command=lambda: confirm_save_window.checker(100, self.frame))
        self.button3 = ttk.Button(self.frame, text="200", command=lambda: confirm_save_window.checker(200, self.frame))
        self.button4 = ttk.Button(self.frame, text="500", command=lambda: confirm_save_window.checker(500, self.frame))
        self.button5 = ttk.Button(self.frame, text="Custom", command=lambda: custom_picker.init_frame(self.frame))
        self.button6 = ttk.Button(self.frame, text="Go Back", command=lambda: account_menu.init_frame(self.frame))

    def init_frame(self, frame):
        clear_previous(frame)
        self.frame.grid()
        self.label1.config(text=f"Choose an amount to {account_menu.move_type}:")
        self.label1.grid(row=0, column=0)
        self.button1.grid(row=0, column=2)
        self.button2.grid(row=1, column=2)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=3, column=2)
        self.button5.grid(row=4, column=2)
        self.button6.grid(row=1, column=0)
        print("▶ Template Picker Screen ◀")


class CustomPicker:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.left_frame = ttk.Frame(self.frame)
        self.label1 = ttk.Label(self.left_frame, text="Dup")
        self.input_text = "0"
        self.user_input = tk.Label(self.left_frame, text="*****", borderwidth=5)
        self.button11 = ttk.Button(self.left_frame, text="Confirm", command=lambda: confirm_save_window.checker(int(self.input_text), self.frame))
        self.button12 = ttk.Button(self.left_frame, text="Go Back", command=lambda: template_picker.init_frame(self.frame))
        self.numpad_frame = ttk.Frame(self.frame, padding=10)

        self.button10 = ttk.Button(self.numpad_frame, text="<-", command=lambda: self.update_numpad(self.user_input, "<"))
        self.button0 = ttk.Button(self.numpad_frame, text="0", command=lambda: self.update_numpad(self.user_input, "0"))
        self.button1 = ttk.Button(self.numpad_frame, text="1", command=lambda: self.update_numpad(self.user_input, "1"))
        self.button2 = ttk.Button(self.numpad_frame, text="2", command=lambda: self.update_numpad(self.user_input, "2"))
        self.button3 = ttk.Button(self.numpad_frame, text="3", command=lambda: self.update_numpad(self.user_input, "3"))
        self.button4 = ttk.Button(self.numpad_frame, text="4", command=lambda: self.update_numpad(self.user_input, "4"))
        self.button5 = ttk.Button(self.numpad_frame, text="5", command=lambda: self.update_numpad(self.user_input, "5"))
        self.button6 = ttk.Button(self.numpad_frame, text="6", command=lambda: self.update_numpad(self.user_input, "6"))
        self.button7 = ttk.Button(self.numpad_frame, text="7", command=lambda: self.update_numpad(self.user_input, "7"))
        self.button8 = ttk.Button(self.numpad_frame, text="8", command=lambda: self.update_numpad(self.user_input, "8"))
        self.button9 = ttk.Button(self.numpad_frame, text="9", command=lambda: self.update_numpad(self.user_input, "9"))

    def update_numpad(self, label, value):
        if value == "<":
            self.input_text = self.input_text[:-2] + "0"
            label.config(text=self.input_text)
        elif not (self.input_text == "0" and value == "0"):
            if len(self.input_text + value) < 13:
                self.input_text = self.input_text[:-1]
                self.input_text += value + "0"
                label.config(text=self.input_text)

    def init_frame(self, frame):
        clear_previous(frame)
        self.frame.grid(row=0, column=0)
        self.left_frame.grid()
        self.label1.config(text=f"Type in custom amount to {account_menu.move_type}:")
        self.label1.grid()
        self.user_input.grid()
        self.numpad_frame.grid(row=0, column=1)
        self.button0.grid(row=4, column=1)
        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)
        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)
        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)
        self.button10.grid(row=4, column=2)
        self.button11.grid()
        self.button12.grid()
        print("▶ Custom Picker Screen ◀")


class ConfirmSaveWindow:
    def __init__(self, win):
        self.frame = ttk.Frame(win, padding=180)
        self.label1 = ttk.Label(self.frame, text="", justify="center")
        self.button1 = ttk.Button(self.frame, text="Go Back", command=lambda: template_picker.init_frame(self.frame))

    def init_frame(self, frame):
        clear_previous(frame)
        user_data.save_userdata()
        txt = f"Process of {account_menu.move_type} confirmed.\n\n" \
              f"Your current account balance is: {user_data.userdata[2]}$\n"
        if account_menu.move_type == "withdraw":
            txt += "\nDon't forget to take Your credit card and cash.\n"
        self.label1.config(text=txt)
        self.frame.grid()
        self.label1.grid()
        self.button1.grid()
        print("▶ Confirmation Screen ◀")

    def checker(self, amount, frame):
        if amount == 0:
            pass
        else:
            if account_menu.move_type == "withdraw" and amount > int(user_data.userdata[2]):
                self.warning_window()
            else:
                if account_menu.move_type == "withdraw":
                    if money_supply.supply_check(amount):
                        user_data.userdata[2] = str(int(user_data.userdata[2]) - amount)
                        confirm_save_window.init_frame(frame)
                elif account_menu.move_type == "deposit":
                    user_data.userdata[2] = str(int(user_data.userdata[2]) + amount)
                    confirm_save_window.init_frame(frame)

    def warning_window(self):
        warning_win = tk.Tk()
        warning_win.title("Warning")
        warning_frame = ttk.Frame(warning_win, padding=40)
        warning_frame.grid()
        ttk.Label(warning_frame, text="You don't have that amount of money to withdraw!").grid()
        ttk.Button(warning_frame, text="Ok", command=warning_win.destroy).grid()


window = tk.Tk()
window.title('ATM Machine 2.0')

# initialize two main objects
user_data = User()
money_supply = MoneySupply()

# initialize specific screen objects
choose_card = ChooseCard(window)
welcome_screen = WelcomeScreen(window)
loading_page = LoadingPage(window)
account_menu = AccountMenu(window)
template_picker = TemplatePicker(window)
confirm_save_window = ConfirmSaveWindow(window)
check_screen = CheckScreen(window)
custom_picker = CustomPicker(window)

# initialize starting screen
welcome_screen.init_frame(False)

window.mainloop()
