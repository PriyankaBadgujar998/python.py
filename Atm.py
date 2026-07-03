class BankAccount:

    BANK_NAME = "SBI"

    def __init__(self, name, mob, age, dob, balance):
        self.name = name
        self.mob = mob
        self.age = age
        self.dob = dob
        self.balance = balance

    def show_info(self):
        print(
            self.name,
            self.mob,
            self.age,
            self.balance
        )

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid Amount")


all_accounts = []

while True:

    print("""
A. Create New Account
B. Check Account Details
C. Deposit Money
D. Withdraw Money
E. Exit
""")

    user_data = input("Enter A Choice: ").upper()

    match user_data:

        case "A":

            name = input("Enter Your Name: ")
            age = int(input("Enter Your Age: "))
            mob = input("Enter Your Mob: ")
            dob = input("Enter Your DOB: ")

            all_accounts.append(
                BankAccount(
                    name=name,
                    mob=mob,
                    dob=dob,
                    age=age,
                    balance=500
                )
            )

        case "B":

            mob = input("Enter Your Mob: ")

            for x in all_accounts:
                if x.mob == mob:
                    print()
                    x.show_info()
                    print()
                    break
            else:
                print("Account Not Found")

        case "C":

            mob = input("Enter Your Mob: ")

            for x in all_accounts:
                if x.mob == mob:

                    amount = int(input("Enter Deposit Amount: "))
                    x.deposit(amount)

                    print()
                    x.show_info()
                    print()
                    break
            else:
                print("Account Not Found")

        case "D":

            mob = input("Enter Your Mob: ")

            for x in all_accounts:
                if x.mob == mob:

                    amount = int(input("Enter Withdraw Amount: "))
                    x.withdraw(amount)

                    print()
                    x.show_info()
                    print()
                    break
            else:
                print("Account Not Found")

        case "E":
            break
