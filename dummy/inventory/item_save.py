#Video time: 1:20:30
import csv
from pathlib import Path

class Item:
    discount = 0.8 # Discount rate
    inventory = [] #46:36
    def __init__(self, name: str, price: float, quantity=0):
        # Validate augments constraint
        assert price >= 0, f"Price {price} cannot be less than 0"
        assert quantity >= 0, f"Price {quantity} cannot be less than 0"
        
        self._name = name
        self.__price = price
        self.quantity = quantity
        
        Item.inventory.append(self)
        
    @property # 1:54:00
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.discount
        
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    @property
    # Property Decorator = Read-only Attribute
    def name(self): # 1:38:00
        return self._name
    
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @classmethod #56:00 decorator
    def instantiate_from_csv(cls): #Class method, the first argument is the class itself i.e. Item
        path =Path(__file__).parent
        with open(f"{path}\\items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity'))
            )
            
    @staticmethod #1:03:30
    def is_integer(num):
        #Check for float number
        if isinstance(num, float):
            return f"Is number a float? {num.is_integer()}"
        elif isinstance(num, int):
            return "Is number an integer? 'True'"
        else:
            return False

    def __repr__(self): #47:30
        # return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        return f"{self.name}('{self.name}', {self.price}, {self.quantity})"
    
    # Read only attributes. Cannot make changes to it
    #Encapsulation 1:34:00
    # @property
    # def read_only_name(self):
    #     return "AAA"
    
#Abstraction 1:58:00
    #Shows neccessary attributes and hides unneccessary ones from the instances
    #Prefix with double underscore makes methods private and can only be called within the class level
    def __connect(self, smtp_server):
        pass
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('10')
        self.__send()