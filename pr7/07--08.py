class ShoppingList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_items(self):
        return self._items

    def clear(self):
        self._items.clear()

shopping = ShoppingList()
shopping.add_item("apple")
shopping.add_item("banana")
print(shopping.get_items())
shopping.clear()
print(shopping.get_items())
