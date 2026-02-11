class MyFineshyt:
    def __init__(self, name, hair, skin):
        self.name = name
        self.hair = hair
        self.skin = skin

    def call(self):
        print("Hey! " + fineshyt.name)

    def how(self):
        print(f"How are you, {fineshyt2.name}?")

fineshyt = MyFineshyt("Alhaitham", "Gray", "Fair")
fineshyt2 = MyFineshyt("Sol", "Black-Green", "Fair")
fineshyt3 = MyFineshyt("Lyney", "White", "Fair")

print(fineshyt.name, fineshyt.hair, fineshyt.skin)
print(fineshyt2.name, fineshyt2.hair, fineshyt2.skin)
print(fineshyt3.name, fineshyt3.hair, fineshyt3.skin)
fineshyt.call()
fineshyt2.how()

fineshyt3.hair = "Gray"
print(fineshyt3.name, fineshyt3.hair, fineshyt3.skin)