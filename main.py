class animal():

    name = ""
    weight = 0
    feed_status = "Голодное"
    voice = ""

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

    goose_1 = goose()
    goose_2 = goose()
    cow_1 = cow()
    ship_1 = ship()
    ship_2 = ship()
    chicken_1 = chicken()
    chicken_2 = chicken()
    goat_1 = goat()
    goat_2 = goat()
    duck_1 = duck()

    goose_1.name = "Серый"
    goose_2.name = "Белый"
    cow_1.name = "Манька"
    ship_1.name = "Барашек"
    ship_2.name = "Кудрявый"
    chicken_1.name = "Ко-Ко"
    chicken_2.name = "Кукареку"
    goat_1.name = "Рога"
    goat_2.name = "Копыта"
    duck_1.name = "Кряква"


    ship_1.voice_check()



main()