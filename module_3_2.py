def is_valid_email(addr: str):
    if "@" not in addr or (addr[-4:] != ".com" and addr[-3:] != ".ru" and addr[-4:] != ".net"):
        return False
    return True


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not is_valid_email(recipient) or not is_valid_email(sender):
        print("Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient)
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
