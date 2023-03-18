class InvalidData(Exception):
    def __init__(self):
        super().__init__("Invalid data type has been detected in the file. The dimentions cannot be less or equal than 0.")

class Rectangle:
    def __init__(self, length, height):
        if length <= 0 or height <= 0:
            raise InvalidData
        self.length = length
        self.height = height

        
    def area(self):
        return self.length * self.height
    
    def __str__(self):
        return f"Prostokąt:\nDługość: {self.length}\nWysokość: {self.height}\nPole powierzchni: {self.area()}"
    
    def __repr__(self):
        return f"Rectangle({self.length}, {self.height})"
    
class Cuboid(Rectangle):
    def __init__(self, length, height, width):
        super().__init__(length, height)
        if (width <= 0):
            raise InvalidData
        self.width = width
        
    def area(self) -> float:
        return round(2 * super().area() + 2 * self.width * self.height + self.width * self.length, 2)
            
    def volume(self) -> float:
        return round(self.length * self.height * self.width, 2)
    
    def __str__(self):
        return f"Prostopadłościan:\nDługość: {self.length}\nWysokość: {self.height}\nSzerokość: {self.width}\nPPP: {self.area()}\nObjętość: {self.volume()}"
    
    def __repr__(self):
        return f"Cuboid({self.length}, {self.height}, {self.width})"
    

if __name__ == "__main__":
    try:
        with open("dane.txt", "r") as file:
            data = file.read()
    except IOError:
        print("Wymagany plik 'dane.txt' nie istnieje. Zamykanie programu.")
        exit()
        
    data = data.split("\n")
        
    for idx, bit in enumerate(data):
        data[idx] = bit.split()
        
    try:    
        for id, bit in enumerate(data):
            for idx, param in enumerate(bit):
                bit[idx] = float(param)
        
    except ValueError:
        print("Wartości nie numeryczne w pliku. Pomijanie wiersza.")
        data.pop(id)
        exit()

    objs = []
    for shape in data:
        try:
            if shape[0] == 1:
                objs.append(Rectangle(shape[1], shape[2]))
            elif shape[0] == 2:
                objs.append(Cuboid(shape[1], shape[2], shape[3]))
        except InvalidData:
            print("Niewłaściwe dane wymiarów. Pomijanie...")
    
        except IndexError:
            print("Niekompletne dane w jednym z wierszy. Pomijanie...")
        
    for obj in objs:
        print(f"{obj}\n")