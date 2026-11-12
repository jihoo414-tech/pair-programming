import threading
from inventory import Inventory, OutOfStock


def test_no_oversell():
    inv = Inventory()
    inv.add("A", 10)
    successes = []

    def worker():
        try:
            inv.reserve("A", 1)
            successes.append(1)
        except OutOfStock:
            pass

    threads = [threading.Thread(target=worker) for _ in range(30)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(successes) == 10
