import time
from queue import Queue
from random import randint
from threading import Thread


class Table:
    def __init__(self, n):
        self.number = n
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def get_first_empty_table(self):
        for table in self.tables:
            if not table.guest:
                return table

    def get_first_occupied_table(self):
        for table in self.tables:
            if table.guest:
                return table

    def guest_arrival(self, *guests):
        for guest in guests:
            # использовать get_first_empty_table каждый раз немного не оптимально, но так проще читается
            if empty_table := self.get_first_empty_table():
                empty_table.guest = guest
                print(f'{empty_table.guest.name} и сел(-а) за стол номер {empty_table.number}')
                guest.start()
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or self.get_first_occupied_table():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
            if (not self.queue.empty()) and (empty_table := self.get_first_empty_table()):
                guest = self.queue.get()
                empty_table.guest = guest
                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {empty_table.number}')
                guest.start()


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
