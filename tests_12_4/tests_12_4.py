import unittest, logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format="%(asctime)s | %(levelname)s | %(message)s", encoding='utf-8')


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_ = Runner('Первый', -10)
            for i in range(10):
                runner_.walk()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner_ = Runner(2)
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = Runner('Третий')
        runner2 = Runner('Четвертый')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
