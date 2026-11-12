import threading
import time


class OutOfStock(Exception):
    pass


class Inventory:
    def __init__(self):
        self._stock = {}

    def add(self, sku, qty):
        self._stock[sku] = self._stock.get(sku, 0) + qty

    def reserve(self, sku, qty):
        lock = threading.Lock()
        with lock:
            current = self._stock.get(sku, 0)
            time.sleep(0.001)  # 디버깅용: 경쟁 상황 재현
            if current < qty:
                raise OutOfStock(sku)
            self._stock[sku] = current - qty
