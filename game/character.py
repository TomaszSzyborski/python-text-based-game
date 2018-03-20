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
        "Strength": 0,
        "Dexterity": 0,
        "Vitality": 0,
        "Magic": 0
    }

    __traits = {
        "Defense": 0,
        "Attack": 0,
        "Damage": 0,#dupcia,
        "Magic Damage": 0
    }

    #Limits
    __item_limit = __attributes

    def __init__(self, attributes):
        self.__inventory = []
        self.__attributes = attributes



    def list_items_in_inventory(self):
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
    dude = Character()

    pretty("Listing items in directory", dude.list_items_in_inventory)

    for item in ["Sword", "Buckler", "Potion"]:
        pretty(f"Putting {item} into inventory", dude.put_into_inventory, f"{item}")

    pretty("Listing items in directory", dude.list_items_in_inventory)

    pretty("Throwing out item nr 3", dude.throw_item_on_the_floor, 3)

    pretty("Listing items in directory", dude.list_items_in_inventory)

