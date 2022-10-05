import math




class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0.00

# Deposit method that accepts an amount and description. If no description is
# given, it should default to an empty string. The method should append an object
# to the ledger list in the form of {"amount": amount, "description": description}.

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': float(amount), 'description': description})
        self.balance += float(amount)

# withdraw method that is similar to the deposit method, but the amount passed in
# should be stored in the ledger as a negative number. If there are not enough funds,
# nothing should be added to the ledger. This method should return True if the 
# withdrawal took place, and False otherwise.

    def withdraw(self, amount, description=''):
        if amount > self.balance:
            return False
        self.ledger.append({'amount': -float(amount), 'description': description})
        self.balance -= float(amount)
        return True

# get_balance method that returns the current balance of the budget category 
# based on the deposits and withdrawals that have occurred.

    def get_balance(self):
        return self.balance

# transfer method that accepts an amount and another budget category as arguments.
# The method should add a withdrawal with the amount and the description 
# "Transfer to [Destination Budget Category]". The method should then add a 
# deposit to the other budget category with the amount and the description 
# "Transfer from [Source Budget Category]". If there are not enough funds, 
# nothing should be added to either ledgers. This method should return True if 
# the transfer took place, and False otherwise.

    def transfer(self, amount, category):
        if amount > self.balance:
            return False
        self.withdraw(amount=amount, description=f'Transfer to {category.name}')
        category.deposit(amount=amount, description=f'Transfer from {self.name}')
        return True
        
# check_funds method that accepts an amount as an argument. It returns False if 
# the amount is greater than the balance of the budget category and returns True
# otherwise. This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
        



# A title line of 30 characters where the name of the category is centered in a line of * characters.
# A list of the items in the ledger. Each line should show the description and amount. 
# The first 23 characters of the description should be displayed, then the amount. 
# The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
# A line displaying the category total.
    def __str__(self):
        first, second = f"{self.name}".center(30, "*"), ""
        for ele in self.ledger:
            desc = ele["description"][:23]
            amount = ele['amount']
            second += f"{desc}{amount: >{len(desc) - 30}.2f}\n"
        second_total = f"Total: {self.balance}"

        return f"{first}\n{second}{second_total}"

    def get_all_withdrawls(self):
        total = 0
        for ele in self.ledger:
            if ele["amount"] < 0:
                total += ele["amount"]

        return round(total, 2)


def create_spend_chart(categories):
    spent, percentages = [], []
    graph = ""
    maxname = 0
    verts = ""
    title = "Percentage spent by category\n"

    for ele in categories:
        spent.append(ele.get_all_withdrawls())

    for amount in spent:
        total = sum(spent)
        percentage = round((amount / total) * 100)
        percentages.append(percentage)

    for interval in range(100, -10, -10):
        graph += str(interval).rjust(3) + "| "
        for percent in percentages:
            if int(percent) >= interval:
                graph += "o  "
            else:
                graph += " " * 3
        graph += "\n"

    graph += " " * 4 + "-" * ((len(categories) * 2) + 4)

    for ele in categories:
        name = ele.name
        if len(name) > maxname:
            maxname = len(name)

    for i in range(maxname):
        if i < maxname:
            verts += "\n" + " " * 5
        for ele in categories:
            name = ele.name
            if len(name) > i:
                verts += name[i] + " " * 2
            else:
                verts += " " * 3

    verts = verts.rstrip("\n")
    return f"{title}{graph}{verts}"