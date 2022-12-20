class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.total = 0

    def deposit(self, amount, description=None):
        self.total += amount
        if description == None:
            self.description = ""
        else:
            self.description = description
        self.ledger.append({"amount": amount, "description": self.description})

    def withdraw(self, amount, description=None):
        if amount > self.total:
            return False
        else:
            self.total -= amount
            if description == None:
                self.description = ""
            else:
                self.description = description
            self.ledger.append(
                {"amount": -amount, "description": self.description}
            )
            return True

    def get_balance(self):
        return self.total

    def transfer(self, amount, other_cat):
        if amount > self.total:
            return False
        else:
            self.total -= amount
            other_cat.total += amount
            print(other_cat)
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": f"Transfer to {other_cat.name}",
                }
            )
            other_cat.ledger.append(
                {"amount": amount, "description": f"Transfer from {self.name}"}
            )
            return True

    def check_funds(self, amount):
        if amount > self.total:
            return False
        else:
            return True

    
