class Inventory(set):
    def print_all_vars(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
        print(40 * "+")


inv = Inventory()

inv.print_all_vars()
inv.sword = "Sword"
inv.print_all_vars()
inv.buckler = "Buckler"
inv.gloves = "Gloves"
inv.shoes = "Shoes"

inv.print_all_vars()

print(f"{80*'@'}\n")


class AtDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


ad = AtDict()
ad.shield= 'Buckler'
ad.weapon = 'Sword'
print(ad)

print(f"{80*'@'}\n")
