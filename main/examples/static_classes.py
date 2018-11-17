
class C(dict):
    __slots__ = []

    def __init__(self, keys, values):
        super().__init__()
        self.update(zip(keys, values))

    def __getattr__(self, key):
        return self[key]


class ReadOnly(dict):
    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value

    def __setattr__(self, name, value):
        raise Exception("It is read only!")



if __name__ == "__main__":
    keys = ['ab', 'cd']
    values = [12, 34]

    c = C(keys, values)
    print(c.ab)
    print(c.cd)
    # throws AttributeError
    # c.ef = 'ef'
    # print(c.ef)

    ro = ReadOnly(["shield", "armor", "weapon"],['buckler', 'hardened leather armor', 'club'])
    print(ro.shield)
    print(ro.armor)
    print(ro.weapon)
    # throws exception
    # ro.shield = "tower shield"

