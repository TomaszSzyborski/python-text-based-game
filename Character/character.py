from Constans.constans import *


class Character:
    """
    Base class for character development
    has
    - inventory
    - attributes
    - traits
    and method describing behaviours
    """

    __inventory = []

    __attributes = {
        STRENGTH: 0,
        DEXTERITY: 0,
        VITALITY: 0,
        PERCEPTION: 0,
        MAGIC: 0
    }

    __traits = {
        "defense": 0,
        "attack": 0,
        "damage": 0,
        "magic_damage": 0
    }

    # Limits
    __item_limit = __attributes

    def __init__(self, name, attributes, character_class):
        self.__character_class = character_class.title()
        self.__name = name.title()
        self.__inventory = []
        self.__attributes = attributes

    @property
    def name(self):
        return self.__name

    @property
    def character_class(self):
        return self.__character_class

    @property
    def strength(self):
        return self.__attributes.get(STRENGTH)

    @property
    def dexterity(self):
        return self.__attributes.get(DEXTERITY)

    @property
    def vitality(self):
        return self.__attributes.get(VITALITY)

    @property
    def perception(self):
        return self.__attributes.get(PERCEPTION)

    @property
    def magic(self):
        return self.__attributes.get(MAGIC)

    # increasing attributes
    def increase_strength(self, value=1):
        self.__attributes[STRENGTH] += value

    def increase_dexterity(self, value=1):
        self.__attributes[DEXTERITY] += value

    def increase_vitality(self, value=1):
        self.__attributes[VITALITY] += value

    def increase_magic(self, value=1):
        self.__attributes[MAGIC] += value

    def increase_perception(self, value=1):
        self.__attributes[PERCEPTION] += value

    # modify invetory
    def list_items_in_inventory(self):
        """
        Prints item number and item name from inventory
        :return:
        """
        for number, item in enumerate(self.__inventory, 1):
            print(number, item)

    def put_into_inventory(self, item):
        """
        Puts given item into inventory

        :param item: - name of the item as string
        :return:
        """
        self.__inventory.append(item)

    def throw_item_on_the_floor(self, item_number):
        """
        Removes and returns item object from inventory
        to be passed into room's floor

        Usage:
        first use list_items_in_inventory to see item numbers

        :param item_number: index of item in inventory
        :return:
        """
        return self.__inventory.pop(item_number - 1)




def pretty(strings, instance_and_method, *args):
    print(strings)
    instance_and_method(*args)


if __name__ == '__main__':
    attributes = {
        STRENGTH: 10,
        DEXTERITY: 15,
        VITALITY: 40,
        PERCEPTION: 17,
        MAGIC: 14
    }

    dude = Character("Dude", attributes, "Warrior")

    print(dude.name)
    print(dude.strength)
    print(dude.dexterity)
    print(dude.vitality)
    print(dude.magic)
    print(dude.perception)
    pretty("Listing items in directory", dude.list_items_in_inventory)

    for item in ["Sword", "Buckler", "Potion"]:
        pretty(f"Putting {item} into inventory", dude.put_into_inventory, f"{item}")

    pretty("Listing items in directory", dude.list_items_in_inventory)

    pretty("Throwing out item nr 3", dude.throw_item_on_the_floor, 3)

    pretty("Listing items in directory", dude.list_items_in_inventory)
