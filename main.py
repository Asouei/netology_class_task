

class animal():

    feed_status = "Голодное"
    voice = ""
    weight_list = []
    weight = 0

    def __init__(self, name, weight, l=weight_list):
        self.name = name
        self.weight = weight
        l = l.append(weight)

    def __add__(self, other):
        return self.weight + other.weight

    def feed(self):

        if self.feed_status == "Голодное":
            self.feed_status = "Сыто"
            print("Животное покормлено")
        else:
            print("Животное не голодно")

    def voice_check(self):

        if self.voice == "ggg":
            print("goose")
        elif self.voice == "muu":
            print("cow")
        elif self.voice == "mee":
            print("ship")
        elif self.voice == "kukareku":
            print("chicken")
        elif self.voice == "bee":
            print("goat")
        elif self.voice == "krya":
            print("duck")




class milk():

    got_milk = "Молока нет"

    def milk(self):

        if self.got_milk == "Молоко есть":
            self.got_milk = "Молока нет"
            print("Молоко добыто")
        else:
            print(self.got_milk)


class egg():

    got_egg = "Яиц нет"

    def egg(self):

        if self.got_egg == "Яйца есть":
            self.got_egg = "Яиц нет"
            print("Яйца добыты")
        else:
            print(self.got_egg)



class goose(animal, egg):
    voice = "ggg"

class cow(animal, milk):
    voice = "muu"

class ship(animal):
    voice = "mee"
    hair = "Нет"

    def cut(self):
        if self.hair == "Есть":
            self.hair = "Нет"
            print("Шерсть добыта")
        else:
            print("Животное не готово к стрижке")

class chicken(animal, egg):
    voice = "kukareku"

class goat(animal, milk):
    voice = "bee"

class duck(animal, egg):
    voice = "krya"


def main():


    goose_1 = goose("Серый", 3.3)
    goose_2 = goose("Белый", 3.1)
    cow_1 = cow("Манька", 400)
    ship_1 = ship("Барашек", 70)
    ship_2 = ship("Кудрявый", 110)
    chicken_1 = chicken("Ко-Ко", 0.4)
    chicken_2 = chicken("Кукареку", 0.3)
    goat_1 = goat("Рога", 38)
    goat_2 = goat("Копыта", 41.4)
    duck_1 = duck("кряква", 1.4)




    def total_weight_check():

        total_weight = 0
        for instance in animal.weight_list:
            total_weight += float(instance)

        print(f'Суммарный вес - {round(total_weight, 2)}')

    total_weight_check()

main()