import pytest
from inventory import Inventory, OutOfStock


def test_reserve_decreases_stock():
    inv = Inventory()
    inv.add("A", 5)
    inv.reserve("A", 2)
    assert inv._stock["A"] == 3


def test_reserve_more_than_stock_raises():
    inv = Inventory()
    inv.add("A", 1)
    with pytest.raises(OutOfStock):
        inv.reserve("A", 2)
