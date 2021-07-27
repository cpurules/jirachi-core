class Item:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount
    
    def __eq__(self, obj):
        return (isinstance(obj, Item) and
                self.id == obj.id and
                self.amount == obj.amount)
    
    def __str__(self):
        return "{0},{1}".format(self.id, self.amount)