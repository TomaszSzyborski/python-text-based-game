class Animal:
    def __init__(self, kolor='czarny', nogi=4, glos="..."):
        self.kolor = kolor
        self.nogi = nogi
        self.glos = glos

    def __getattr__(self, name):
        print(f"Creating attribute {name}.")
        setattr(self, name, None)
        return None

    def daj_glos(self):
        print(self.glos)


class Krowa(Animal):
    def __init__(self, rogi=2):
        self.rogi=rogi
        super(Krowa, self).__init__(glos="Muuuu!!!")


a = Animal()
a.daj_glos()
print(f"Rogi: {a.rogi}")

c = Krowa()
c.daj_glos()
print(f"Rogi: {c.rogi}")


print(f"Plamy: {c.plamy}")
print(f"Agamy: {c.agamy}")

print(f"Plamy: {c.plamy}")
print(f"Agamy: {c.agamy}")

c.plamy = 3
c.agamy = 4
print(f"Plamy: {c.plamy}")
print(f"Agamy: {c.agamy}")
