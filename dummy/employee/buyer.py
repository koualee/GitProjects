import employee
from inventory.item import Item

class create_inventory(Item):
    def __init__(self, name: str, price: int, quantity=0):
        super().__init__(name, price, quantity)

koua = employee.Employee('koua', 'lee', 80)

add_item = create_inventory('iphone', 500, 5)

Item.instantiate_from_csv()

def get_inventory():
    inventory_dict = {}
    for i in Item.inventory:
        inventory_list = [i.name, i.price, i.quantity]
        inventory_dict[i.name] = inventory_list
    return inventory_dict

# def update_low_inventory(qty):
    
def update_low_inventory():
    inventory = get_inventory()
    for k, v in inventory.items():
        v[2] += 10 if v[2] <= 2 else v[2]
        inventory[k] = v
    print (inventory)
    
update_low_inventory()

