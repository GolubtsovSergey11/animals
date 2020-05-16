
class Animals():

    total_weight = []
    max_weight = 0
    max_weight_name = 0

    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.total_weight.append(weight)
        if self.max_weight < self.weight:
            Animals.max_weight = self.weight
            Animals.max_weight_name = self.name

    def feed(self):
        self.state = 'кормить'
        return self.state


class Cow(Animals):

    def cow_milk(self):
        self.state = 'Доить'
        return self.state


class Goat(Cow, Animals):

    pass


class Sheep(Animals):

    def to_cut(self):
        self.state = 'Стрич'
        return self.state


class Chicken(Animals):

    def pick_eggs_chicken(self):
        self.state = 'собирать яйца'
        return self.state


class Duck(Chicken, Animals):

    pass


class Goose(Chicken, Animals):

    pass


sheep1 = Sheep(name='Барашек', weight=100, sound=',бекает')
sheep2 = Sheep(name='Кудрявый', weight=103, sound='бекает')
duck = Duck(name='Кряква', weight=20, sound='кря кря')
chicken1 = Chicken(name='Ко-ко', weight=12, sound='ко-ко')
chicken2 = Chicken(name='Кукареку', weight=15, sound='ко-ко-ко')
goose1 = Goose(name='Серый', weight=11, sound='гагага')
goose2 = Goose(name='Белый', weight=13, sound='га-га-га')
cow = Cow(name='Манька', weight=500, sound='мычит')
goat1 = Goat(name='Рога', weight=20, sound='бебебе')
goat2 = Goat(name='Копыта', weight=18, sound='бебебе')

print(f'Общий вес всех животных {sum(Animals.total_weight)} кг.')
print(f'Самое тяжелое животное по имени {Animals.max_weight_name}, весит {Animals.max_weight} кг.')