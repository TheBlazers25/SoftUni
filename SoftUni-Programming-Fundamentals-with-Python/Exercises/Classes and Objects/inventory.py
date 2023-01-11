class Inventory:

    items = []

    def __init__(self, __capacity: int):
        self.__capacity = __capacity

    def add_item(self, item: str):
        self.capacity_left = self.__capacity
        if self.__capacity > 0:
            Inventory.items.append(item)
            self.capacity_left -= self.__capacity
        return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(Inventory.items)}.\nCapacity left: {self.capacity_left}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)