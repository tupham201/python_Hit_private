class manu:
    def __init__(self,indentity, location):
        self.indentity = indentity
        self.location = location
    def InTT(self):
        print(f"Indentity: {self.indentity} - Location: {self.location}")

class Device(manu):
    def __init__(self,name, price, indentity, location):
        self.name = name
        self.price = price
        super().__init__(indentity, location)
    def InTT(self):
        print(f"Name: {self.name} - Price: {self.price}")
        super().InTT()

de = Device(name="mouse", price=2.5, indentity=9725, location="Viet nam")
de.InTT()
print()
de1 = Device(name="monitor", price=12.5, indentity=11, location="Germany")
de1.InTT()