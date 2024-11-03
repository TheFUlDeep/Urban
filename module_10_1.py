import time
import datetime
from threading import Thread


def write_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write('Какое-то слово № ' + str(i + 1) + '\n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


started_at = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f'Работа потоков {datetime.timedelta(seconds=time.time() - started_at)}')

started_at = time.time()
t1 = Thread(target=write_words, args=(10, 'example5.txt'))
t2 = Thread(target=write_words, args=(30, 'example6.txt'))
t3 = Thread(target=write_words, args=(200, 'example7.txt'))
t4 = Thread(target=write_words, args=(100, 'example8.txt'))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(f'Работа потоков {datetime.timedelta(seconds=time.time() - started_at)}')
