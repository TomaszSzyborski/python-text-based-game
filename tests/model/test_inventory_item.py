from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest
from pytest import fixture

from main.model.inventory_item import InventoryItem
import logging

from tests.model import constants_inventory_item

log = logging.getLogger("LOGGER")

@fixture
def item():
    return InventoryItem(name=constants_inventory_item.NAME,
                         unit_price=constants_inventory_item.UNIT_PRICE)


def test_item_name_set_in_constructor(item):
    assert item.name == "puklerz"


def test_item_name_set_in_runtime(item):
    with pytest.raises(FrozenInstanceError):
        item.name = "miecz"
    assert item.name == "puklerz"
