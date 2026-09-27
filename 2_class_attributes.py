# Concept: class attribute (shared) vs instance attribute (unique)
# Example: BankAccount 

class BankAccount:
    # --- class attributes: shared by EVERY object of this class ---
    bank_name = "CodeBank Pakistan"
    interest_rate = 0.05          # 5% yearly
    accounts_created = 0          # acts as a counter for all accounts

    def __init__(self, owner, balance):
        # --- instance attributes: unique to each object ---
        self.owner = owner
        self.balance = balance
        # note: this only increments for this instance...
        BankAccount.accounts_created += 1  # ...but we update the CLASS attribute

    # instance method using both kinds of attributes
    def show_account(self):
        print(f"Owner   : {self.owner}")
        print(f"Balance : Rs. {self.balance}")
        print(f"Bank    : {self.bank_name} (class attribute)")
        print(f"Rate    : {BankAccount.interest_rate * 100}% (class attribute)")

    # instance method that changes the instance's own state
    def deposit(self, amount):
        self.balance += amount
        print(f"  Deposited Rs. {amount} -> new balance Rs. {self.balance}")

    # instance method reading the class-level counter
    def total_accounts(self):
        print(f"  Total accounts created so far: {BankAccount.accounts_created}")


if __name__ == '__main__':
    acc1 = BankAccount("Muhammad Saad Khan", 25000)
    acc2 = BankAccount("Ali Hassan", 8000)

    print("--- Account 1 ---")
    acc1.show_account()
    acc1.deposit(5000)
    acc1.total_accounts()
    print()

    print("--- Account 2 ---")
    acc2.show_account()
    acc2.total_accounts()
    print()

    # proof: class attribute is shared, instance attributes are not
    print(f"acc1.bank_name == acc2.bank_name ? {acc1.bank_name == acc2.bank_name}")
    print(f"acc1.balance   == acc2.balance   ? {acc1.balance == acc2.balance}")
    print(f"Both accounts belong to the same bank name object: "
          f"{acc1.bank_name is acc2.bank_name}")
