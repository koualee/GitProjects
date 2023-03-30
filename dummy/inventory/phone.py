from item import Item

class Phone(Item):
    phone_list = [] #1:20:30
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Initialize super class
        super().__init__(name, price, quantity)
        # Validate augments constraint
        assert broken_phones >= 0, f"Broken phones {broken_phones} cannot be less than 0"

        # Assign to self object
        self.broken_phones = broken_phones
        