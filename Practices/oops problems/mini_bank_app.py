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
    def deposit_amount(self,damt, acc_no):
        for customer in self.customers.values():
            print(customer["name"],customer["Account No"],acc_no,)
            if customer["Account No"] == acc_no:
                customer["balance"] += damt
                print("Your balance have been deposit successfully")
                print("Account No:", acc_no)
                print("New Balance:", customer["balance"])
            else:
                print("Customer not exist")
        return False

    # ---------- CREATE ACCOUNT ----------
    def create_account(self, name, email, phone, initial_balance=0):

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
        }

        print("✅ Account created successfully")
        print("Account No:", account_number)
        print("Name:", name)
        print("Balance:", initial_balance)

        return account_number

    def deposit_balance(self,damt, acc_no):
        self.deposit_amount(damt, acc_no)

    def check_balance(self, acc_no):
        if acc_no in self.customers:
            print("\n💰 Current Balance:", self.customers[acc_no]["balance"])
        else:
            print("❌ Account not found")


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
    inp_ac_no = int(input("Enter your Account number:"))
    damt = int(input("Enter deposit amount in existing amount: "))

    bank.deposit_balance(damt=damt, acc_no=inp_ac_no)
    inp_ac_no = int(input("Enter your Account number:"))
    bank.check_balance(inp_ac_no)
