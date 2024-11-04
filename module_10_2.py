from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power, enemies=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while (self.enemies > 0):
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            print(f'{self.name} сражается {self.days} день(дней), осталось {self.enemies} войнов')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
