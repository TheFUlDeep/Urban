from time import sleep


class User:
    def __init__(self, nickname, password, age=0):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        # в ТЗ не было сказано добавлять этот атрибут
        self.users_dict = {}
        # аналогично с видео
        self.videos_dict = {}
        # правда из-за этого у меня по сути не используются списки self.users и self.videos
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users_dict and self.users_dict[nickname].password == hash(password):
            self.current_user = self.users_dict[nickname]

    def register(self, nickname, password, age):
        if nickname in self.users_dict:
            print(f'Пользователь {nickname} уже существует')
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.current_user = user
            self.users_dict[user.nickname] = user

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i.title in self.videos_dict:
                continue
            self.videos.append(i)
            self.videos_dict[i.title] = i

    def get_videos(self, title):
        # поиск без авторизации разрешен
        res = []
        for k, v in self.videos_dict.items():
            if title.lower() in k.lower():
                res.append(k)
        return res

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if not title in self.videos_dict:
            return
        cur_vid = self.videos_dict[title]
        if cur_vid.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        while cur_vid.time_now < cur_vid.duration:
            print(cur_vid.time_now + 1, end=" ")
            sleep(0.3)
            cur_vid.time_now += 1
        print("Конец видео")

        cur_vid.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
