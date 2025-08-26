class Category:


    def __init__(self, category):
        self.category = category
        self.ledger = []


    def __str__(self):
        ledgerl= ""
        for x in self.ledger:
            description = x['description'][:23].ljust(23)
            amount = f"{x['amount']:.2f}".rjust(7)
            ledgerl += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{self.category.center(30, '*')}\n" + ledgerl + total
        



#deposit
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

#withdrawal
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})
            return True
        else:
            return False

#get_balance
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
      
#check_balance
    def check_funds(self, amount):
            if amount > self.get_balance():
                return False
            else:
                return True

#transfer
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False




def create_spend_chart(categories):
    
    spent_amounts = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += abs(item['amount'])
        spent_amounts.append(spent)

    print(spent_amounts)
    chart = ''
    total_spent = sum(spent_amounts)

    spent_percentages = []

    for amount in spent_amounts:
        percentage = (amount / total_spent) * 100
        spent_percentages.append(abs(percentage))


    for percent in range(100, -1, -10):
        chart += str(percent).rjust(3)+ '| '
        for percentage in spent_percentages:
            if (percentage // 10) * 10 >= percent:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    ' + '---' * len(categories) + '-'
    print(spent_percentages)

    max_len = max(len(cat.category) for cat in categories)
    for i in range(max_len):
        line = '     '  # Pięć spacji na początek linii
        for category in categories:
            if i < len(category.category):
                line += category.category[i] + '  '
            else:
                line += '   '
        chart += '\n' + line
        
    return f'Percentage spent by category\n{chart}'


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(40.12, 'nie')
print(food)


print(create_spend_chart([food, clothing]))
