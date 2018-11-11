import pytest
from pytest import fixture

from main.model.character import Character
import logging

log = logging.getLogger("LOGGER")

@fixture
def character():
    return Character({
        "Strength": 10,
        "Dexterity": 10,
        "Vitality": 10,
        "Magic": 10
    })


@fixture
def character_with_items():
    c = Character({
        "Strength": 10,
        "Dexterity": 10,
        "Vitality": 10,
        "Magic": 10
    })
    c.put_into_inventory("Buckler")
    c.put_into_inventory("Sword")
    return c


def test_add_item_to_inventory(character):
    log.info(f"Inventory: {character.inventory}")
    assert character.inventory == []
    for index, item in enumerate(["Sword", "Buckler", "Potion"]):
        character.put_into_inventory(item)
        assert len(character.inventory) == index + 1


def test_drop_item_on_the_floor(character_with_items):
    assert len(character_with_items.inventory) == 2
    character_with_items.drop_item_on_the_floor(2)
    assert len(character_with_items.inventory) == 1
    character_with_items.drop_item_on_the_floor(1)
    assert len(character_with_items.inventory) == 0
    with pytest.raises(IndexError):
        character_with_items.drop_item_on_the_floor(1)
