import random, threading, time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rnd_num = random.randrange(50, 500)
            self.balance += rnd_num
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rnd_num}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rnd_num = random.randint(50, 500)
            print(F'Запрос на {rnd_num}')
            if rnd_num <= self.balance:
                self.balance -= rnd_num
                print(f'Снятие: {rnd_num}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
