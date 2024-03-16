from BalanceInAtm import Balance
from authentication import Authentication

class ATM:
    def __init__(self):
        BalanceObject = Balance()
        self.available_amount_in_atm = BalanceObject.BalanceValue()
        self.card_types_list = ["rupay", "visa", "master"]
        self.transactions_list = []
        self.account_balance = 7000

    def get_account_type(self):
        self.limit_amount = 0
        while True:
            self.account_type = input("Select the account type (rupay/master/visa): ")
            if self.account_type not in self.card_types_list:
                continue
            else:
                self.set_account_limit()
                AuthenticationObject = Authentication()
                AuthenticationObject.Login()
                break

    def get_the_balance(self):
        print("The available amount in ATM is:", self.available_amount_in_atm)

    def set_account_limit(self):
        if self.account_type == "rupay":
            self.limit_amount = 2000
        elif self.account_type == "master":
            self.limit_amount = 5000
        else:
            self.limit_amount = 8500
        print("Your limit is", self.limit_amount)

    def get_balance_of_user(self):
        print("Balance:", self.account_balance)

    def cash_withdrawal(self):
        self.withdrawal_amount = int(input("Enter the amount to withdraw: "))
        if self.withdrawal_amount <= self.limit_amount and self.withdrawal_amount <= self.account_balance:
            self.account_balance -= self.withdrawal_amount
            self.transactions_list.append(str(self.withdrawal_amount) + " debited")
            print(self.transactions_list)
        else:
            print("Insufficient funds or limit exceeded")

    def cash_deposit(self):
        self.deposit_amount = int(input("Enter the deposit amount: "))
        self.account_balance += self.deposit_amount
        self.transactions_list.append(str(self.deposit_amount) + " credited")
        print(self.transactions_list)

    def get_choice_of_user(self):
        self.user_choice_input = int(input("Enter your choice: "))

    def print_mini_statement(self):
        list_t = self.transactions_list[::-1]
        for i in list_t:
            print(i)

    def operate(self):
        while True:
            print("Options:")
            print("1. Check Balance")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Mini Statement of Last 3 Transactions")
            print("5. Exit")
            self.get_choice_of_user()
            if self.user_choice_input == 1:
                self.get_balance_of_user()
            elif self.user_choice_input == 2:
                self.cash_withdrawal()
            elif self.user_choice_input == 3:
                self.cash_deposit()
            elif self.user_choice_input == 4:
                self.print_mini_statement()
            elif self.user_choice_input == 5:
                print("Thank you for using our ATM. Have a nice day!")
                break
            else:
                print("Enter a valid input!")

person1 = ATM()
person1.get_the_balance()
person1.get_account_type()
person1.operate()
