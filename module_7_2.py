def custom_write(file_name, strings):
    # очистка файла
    f = open(file_name, 'w')
    f.write("")
    f.close()

    strings_positions = dict()
    f = open(file_name, 'a', encoding='utf-8')
    n = 1
    for s in strings:
        strings_positions[(n,f.tell())] = s
        f.write(s + "\n")
        n +=1
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
