import random
import re


class Bank:
    def __init__(self):
        self.customers = {}

    # -----Check email validation ----
    def is_valid_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email)

    # ---check email exist -------
    def email_exist(self, email):
        for customer in self.customers.values():
            print(customer)
            if customer["email"] == email:
                return True
        return False

    # ---------- CHECK PHONE EXISTS ----------
    def phone_exists(self, phone):
        for customer in self.customers.values():
            if customer["phone"] == phone:
                return True
        return False

    def generate_account_number(self):
        while True:
            acc_no = int(random.randint(10**13, 10**14 - 1))
            if acc_no not in self.customers:
                return acc_no

    # ---------- deposit amount ------
    def deposit_amount(self, acc_no, damt):

        if acc_no not in self.customers:
            print("❌ Account number does not exist")
            return False

        self.customers[acc_no]["balance"] += damt
        print("✅ Deposit successful")
        print("Account No:", acc_no)
        print("New Balance:", self.customers[acc_no]["balance"])
        return True


    # ---------- CREATE ACCOUNT ----------
    def create_account(self, name, email, phone, initial_balance=0, pin=None):

        if not self.is_valid_email(email):
            print("❌ Invalid email format")
            return

        if self.email_exist(email):
            print("❌ This email is already registered")
            return

        if self.phone_exists(phone):
            print("❌ This phone number is already registered")
            return

        account_number = self.generate_account_number()

        self.customers[account_number] = {
            "name": name,
            "email": email,
            "phone": phone,
            "balance": initial_balance,
            "Account No": account_number,
            "pin": pin,
        }

        print("✅ Account created successfully")
        print("Account No:", account_number)
        print("Name:", name)
        print("Balance:", initial_balance)

        return account_number

    def deposit_balance(self, damt, acc_no):
        self.deposit_amount(damt, acc_no)

    def check_balance(self, acc_no):
        if acc_no in self.customers:
            print("💰 Current Balance:", self.customers[acc_no]["balance"])
        else:
            print("❌ Account not found")

    def create_atm_pin(self, acc_no, pin):
        pin = str(pin)  # convert to string to count digits

        if len(pin) != 4:
            print("❌ PIN must be exactly 4 digits")
            return False

        if acc_no not in self.customers:
            print("❌ Account does not exist")
            return False

        self.customers[acc_no]["pin"] = pin
        print("✅ ATM PIN created successfully")
        return True

    def verify_pin(self, acc_no, pin):
        if acc_no not in self.customers:
            print("❌ Account does not exist")
            return False
        if self.customers[acc_no]["pin"] == str(pin):
            print("✅ Your PIN is verified! now please enter amount")
            return True
        else:
            print("❌ Incorrect PIN")
            return False

    def withdraw_amount(self, acc_no, amount):

        if amount > self.customers[acc_no]["balance"]:
            print("❌ Insufficient balance")
            return False

        self.customers[acc_no]["balance"] -= amount
        print("✅ Withdrawal successful")
        print("Remaining Balance:", self.customers[acc_no]["balance"])
        return True


# create an instance
bank = Bank()
print("\n--- CREATE NEW ACCOUNT ---")

name = input("Enter your name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
balance = int(input("Enter initial deposit amount: "))
acc_no = bank.create_account(
    name=name, email=email, phone=phone, initial_balance=balance
)

if acc_no:
    print("\n⚠️ Please save your account number:", acc_no)
    print("\n--- DEPOSIT MONEY ---")

    while True:
        inp_ac_no = int(input("Enter your Account number: "))

        if inp_ac_no in bank.customers:
            break
        else:
            print("❌ Wrong account number. Please try again!")

    damt = int(input("Enter deposit amount: "))

    bank.deposit_amount(inp_ac_no, damt)

    print("\n--- Check Balance ---")
    inp_ac_no = int(input("Enter your Account number for check your balance:"))
    bank.check_balance(inp_ac_no)

    # ----- Create your atm PIN first then withdraw amount ----
    while True:
        print("\n--- Create your ATM PIN ---")
        atm_pin = input("Enter 4-digit ATM PIN: ")
        if bank.create_atm_pin(inp_ac_no, atm_pin):
            break
    # ----Verify ATM PIN ---
    print("\n---Verify your ATM PIN first then withdraw amount ---")
    while True:
        withdraw_acc_no = int(input("Enter your Account Number: "))
        pin = input("Enter your PIN: ")
        # Step 1: Check PIN
        if bank.verify_pin(withdraw_acc_no, pin):
            break  # PIN correct → exit loop
    # ----withdraw amount ---

    while True:
        amount = int(input("Enter your amount: "))

        if bank.withdraw_amount(acc_no, amount):
            break  # stop after successful withdrawal
