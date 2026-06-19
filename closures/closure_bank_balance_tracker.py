def bank_balance():
    balance = 1000
    def bank_operation(operation, inp_amount = 0):
        def deposit(amount):
            nonlocal balance
            balance += amount
            balance_check()
        def withdraw(amount):
            nonlocal balance
            balance -= amount
            balance_check()
        def balance_check():
            print(balance)

        match operation:
            case 'deposit':
                deposit(inp_amount)
            case 'withdraw':
                withdraw(inp_amount)
            case 'balance':
                balance_check()

    return bank_operation

bank = bank_balance()
bank('deposit', 500)
bank('withdraw', 300)
bank('balance')