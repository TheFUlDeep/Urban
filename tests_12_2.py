import unittest, pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        # исправление логической ошибки (сортировка по пройденной дистанции)
        finishers = sorted(finishers.items(), key=lambda x: x[1].distance, reverse=True)
        return {place + 1: finishers[place][1] for place in range(len(finishers))}


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_results)

    def test_1_3(self):
        tournament_ = Tournament(90, self.runner1, self.runner3).start()
        self.all_results.append({place: participant.name for place, participant in tournament_.items()})
        self.assertTrue(tournament_[len(tournament_)] == 'Ник')

    def test_2_3(self):
        tournament_ = Tournament(90, self.runner2, self.runner3).start()
        self.all_results.append({place: participant.name for place, participant in tournament_.items()})
        self.assertTrue(tournament_[len(tournament_)] == 'Ник')

    def test_1_2_3(self):
        tournament_ = Tournament(90, self.runner1, self.runner2, self.runner3).start()
        self.all_results.append({place: participant.name for place, participant in tournament_.items()})
        self.assertTrue(tournament_[len(tournament_)] == 'Ник')

    def test_logic(self):
        tournament_ = Tournament(1, self.runner1, self.runner2, self.runner3).start()
        self.all_results.append({place: participant.name for place, participant in tournament_.items()})
        self.assertTrue(tournament_[len(tournament_)] == 'Ник')



if __name__ == "__main__":
    unittest.main()
