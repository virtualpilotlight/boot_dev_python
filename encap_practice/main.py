class BankAccount:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self) -> str:
        return self.__account_number

    def get_balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        #print("in deposit")
        if amount <= 0.00:
            #print("in deposit if")
            raise ValueError("cannot deposit zero or negative funds")
        else:
            self.__balance += amount

    def withdraw(self, amount: float) -> None:
        print("in withdraw")
        print(amount)
        if amount <= 0.00:
            print("in 2nd if amount less than 0")
            raise ValueError("cannot withdraw zero or negative funds")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount
