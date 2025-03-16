
class Base:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def change(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def get_pairs(self, data):
        pairs = list(data.items())[:2]
        keys = {pairs[0][0], pairs[1][0]}
        values = {str(pairs[0][1]), str(pairs[1][1])}
        return keys, values

class Child(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

obj = Base(1, 2)
print(obj.a, obj.b)

obj.change(3, 4)
print(obj.a, obj.b)

d = {"x": 5, "y": "hello", "z": [1, 2]}
k, v = obj.get_pairs(d)
print("Ключі:", k)
print("Значення:", v)
