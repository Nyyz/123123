import random

class Parent:
    def __init__(self, name):
        self.name = name

    def get_random_pairs(self):
        data: dict[str, int | str | bool | list[str] | float] = {
            "age": 25, "height": 175.5, "city": "Kyiv",
            "is_student": True, "hobbies": ["reading", "sports"], "id": 101
        }

        items = dict(random.sample(list(data.items()), random.randint(1, len(data))))

        keys = set(items.keys())
        values = [str(v) if isinstance(v, (list, dict, set)) else v for v in items.values()]

        return keys, values

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


child = Child("Анна", 25)
keys, values = child.get_random_pairs()

print("Ключі:", keys)
print("Значення:", values)
