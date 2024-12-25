import unittest, tests_12_3.tests_12_1 as tests_12_1, tests_12_3.tests_12_2 as tests_12_2

# чтобы не изменять "оригинальные" файлы классов, пишу добавление атрибутов и декоратор здесь отдельно
tests_12_1.RunnerTest.is_frozen = False
tests_12_2.TournamentTest.is_frozen = True


def skip_decorator(f):
    def surrogate(*args, **kwargs):
        if args[0].is_frozen:
            raise unittest.SkipTest("Тесты в этом кейсе заморожены")
        else:
            return f(*args, **kwargs)

    return surrogate


tests_12_1.RunnerTest.test_walk = skip_decorator(tests_12_1.RunnerTest.test_walk)
tests_12_1.RunnerTest.test_run = skip_decorator(tests_12_1.RunnerTest.test_run)
tests_12_1.RunnerTest.test_challeng = skip_decorator(tests_12_1.RunnerTest.test_challeng)
tests_12_2.TournamentTest.test_1_3 = skip_decorator(tests_12_2.TournamentTest.test_1_3)
tests_12_2.TournamentTest.test_2_3 = skip_decorator(tests_12_2.TournamentTest.test_2_3)
tests_12_2.TournamentTest.test_1_2_3 = skip_decorator(tests_12_2.TournamentTest.test_1_2_3)
tests_12_2.TournamentTest.test_logic = skip_decorator(tests_12_2.TournamentTest.test_logic)

calcST = unittest.TestSuite()

calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

text_test_runner = unittest.TextTestRunner(verbosity=2)

if __name__ == "__main__":
    text_test_runner.run(calcST)
