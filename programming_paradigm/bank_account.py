class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default is 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient. Return True if successful, False otherwise."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
