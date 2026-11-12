class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self):
        self._stock = {}

    def add(self, sku, qty):
        self._stock[sku] = self._stock.get(sku, 0) + qty

    def reserve(self, sku, qty):
        current = self._stock.get(sku, 0)
        if current < qty:
            raise OutOfStock(sku)
        self._stock[sku] = current - qty
