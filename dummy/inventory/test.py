from inventory.item import Item
from inventory.phone import Phone


# Item.instantiate_from_csv()

item1 = Item('MyItem', 750, 6)
# print (f"the first name is {item1.name}")
# item1.price = 900
# print (item1.name)

#Encapsulation 1:51:00
    #Restricting direct access to attributes in a program
# item1.apply_increment(0.2)
# print (item1.price)

# item1.apply_discount()
# print (item1.price)

#Abstraction 1:58:00
    #Shows neccessary attributes and hides unneccessary ones from the instances
    #Prefix with double underscore makes methods private and can only be called within the class level
    
# item1.send_email()
    
#Inheritance 2:03:30
    #Allows reuse of codes across classes
    
#Polymorphism 2:06:00
    #Use of a single type of entity ro represent different types in different scenarios
    
    
phone1 = Phone('iPhone', 500, 10)
print (phone1.price)
phone1.apply_discount()
print (phone1.price)

print (phone1.calculate_total_price())

