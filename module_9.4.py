# "Создание функций на лету"
# Задача "Функциональное разнообразие"


from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

# lambda-функция, результат которой - список совпадения букв в той же позиции
print(list(map(lambda lit1, lit2: lit1 == lit2, first, second)))


# функция принимает название файла для записи, возвращает функцию write_everything
def get_advanced_writer(file_name):

    # добавляет в файл file_name все данные из data_set в том же виде.
    # data_set - параметр принимающий неограниченное количество данных любого типа.
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'{data_set}')
        return
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

write_ = get_advanced_writer('example_.txt')
write_('Это', 1, 'cловарь', [{1:'one', 2: "two"}, ('и','ещё','кортеж'), 'всё в списке'])
write_('А это', 'дополнительно', 'N', 2)


class MysticBall:
    def __init__(self, *words):         # words - коллекция строк
        self.words = words

 # метод случайным образом выбирает слово из words и возвращает его
    def __call__(self):                
        return choice(self.words)


# Класс здесь
first_ball = MysticBall('Всегда', 'Часто', 'Иногда', 'Редко','Никогда')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
