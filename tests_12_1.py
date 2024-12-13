import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_ = Runner('Первый')
        for i in range(10):
            runner_.walk()
        self.assertEqual(runner_.distance, 50)

    def test_run(self):
        runner_ = Runner('Второй')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challeng(self):
        runner1 = Runner('Третий')
        runner2 = Runner('Четвертый')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
