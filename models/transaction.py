class Transaction:

    def __init__(self, name, description, amount, date, tag = None, merchant = None, id = None):
        self.name = name
        self.description = description
        self.amount = amount
        self.date = date
        self.tag = tag
        self.merchant = merchant
        self.id = id