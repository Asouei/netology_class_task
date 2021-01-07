

class animal():

    feed_status = "Голодное"
    voice = ""
    weight_list = []
    weight = 0
    name_weight_dict = dict()
    name_type_dict = dict()


    def __init__(self, name, weight, w=weight_list, d = name_weight_dict, t=name_type_dict):
        self.name = name
        self.weight = weight
        t_ = self.type
        w = w.append(weight)

        d[name] = weight
        t[name] = t_

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
    type = 'гусь'


class cow(animal, milk):
    voice = "muu"
    type = 'корова'

class ship(animal):
    voice = "mee"
    hair = "Нет"
    type = 'овца'

    def cut(self):
        if self.hair == "Есть":
            self.hair = "Нет"
            print("Шерсть добыта")
        else:
            print("Животное не готово к стрижке")

class chicken(animal, egg):
    voice = "kukareku"
    type = 'курица'

class goat(animal, milk):
    voice = "bee"
    type = 'коза'

class duck(animal, egg):
    voice = "krya"
    type = 'утка'

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

    def weight_biggest():
        weight_ = 0
        name = ""
        type_ = ""

        for n, w in animal.name_weight_dict.items():
            if weight_ < w:
                weight_ = w
                name = n
        for n, t in animal.name_type_dict.items():
            if name == n:
                type_ = t

        print(f'Самое тяжелове животное - {name}. Это - {type_}. Вес - {weight_}кг.')

    total_weight_check()
    weight_biggest()

main()