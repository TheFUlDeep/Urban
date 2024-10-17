class WordsFinder:
    __CHARS_TO_REMOVE = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_names):
        self.file_names = file_names

    def __remove_characters(self, string):
        res = string
        for char in self.__CHARS_TO_REMOVE:
            while char in res:
                res = str.replace(string, char, "")
        return res

    def get_all_words(self):
        all_words = dict()
        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                all_words[filename] = self.__remove_characters(f.read().lower()).split()
        return all_words

    def find(self, word):
        res = dict()
        for filename, words in self.get_all_words().items():
            for n in range(len(words)):
                if word.lower() == words[n]:
                    res[filename] = n + 1
                    break
        return res

    def count(self, word):
        res = dict()
        for filename, words in self.get_all_words().items():
            for n in range(len(words)):
                if word.lower() == words[n]:
                    if not filename in res:
                        res[filename] = 1
                    else:
                        res[filename] += 1
        return res



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
