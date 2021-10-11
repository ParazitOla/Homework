### Task 6.4 Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
# Implement str() function call for each class.

class Bird:
    # * class `Bird` with an attribute `name` and methods `fly` and `walk`.

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} bird can walk and fly'

    def fly(self):
        return print(f'{self.name} bird can fly')

    def walk(self):
        return print(f'{self.name} bird can walk')


# b = Bird("Any")
# b.walk()
# b.fly()
# print(str(b))


class FlyingBird(Bird):
    # * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
    # Implement the method `eat` which will describe its typical ration.
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return print(f'It eats mostly {self.ration}')


# c = FlyingBird("Canary")
# print(str(c))
# c.walk()
# c.fly()
# c.eat()


class NonFlyingBird(Bird):
    # * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
    # Add same "eat" method but with other implementation regarding the swimming bird tastes.

    def __init__(self, name, ration):
        super().__init__(name)
        self.ration = ration

    def __getattribute__(self, name):
        if name in ['fly']:
            raise AttributeError(f"'{self.name}' object has no attribute 'fly'")
        return super(NonFlyingBird, self).__getattribute__(name)

    def swim(self):
        return print(f'{self.name} bird can swim')

    def eat(self):
        return print(f'It eats mostly {self.ration}')

    def __str__(self):
        return f'{self.name} bird can walk and swim'


# p = NonFlyingBird("Penguin", "fish")
# p.swim()
# p.fly()
# p.eat()
# print(str(p))


class SuperBird(NonFlyingBird):
    # * class `SuperBird` which can do all of it: walk, fly, swim and eat.
    # But be careful which "eat" method you inherit.
    def __init__(self, name, *ration):
        super().__init__(name, ration)
        self.ration = ration

    def __str__(self):
        return f'{self.name} bird can walk, swim and fly'

    def eat(self):
        return print(f'It eats fish')


s = SuperBird("Gull")
print(str(s))
s.eat()
