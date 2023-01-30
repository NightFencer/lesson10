# -*- coding: utf-8 -*-
import datetime
import os.path


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть,
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
def line_checker(name, email, age):
    result = 'NOk'

    if not name.isalpha():
        raise NotNameError('имя не из букв')
    elif not ('@' in email and '.' in email):
        raise NotEmailError('email без точки или собаки')
    elif not 9 < int(age) < 100:
        raise ValueError('возраст нереальный')
    else:
        result = 'Ok'

    return result


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass

t0 = datetime.datetime.now()
file = 'C:\\Users\\DellWorkStation\\PycharmProjects\\TelegramBots\\pythonProject\\lesson10\\registrations.txt'
good_reg_file = 'registrations_good.log'
bad_reg_file = 'registrations_bad.log'
f1, f2 = open(good_reg_file, 'w', encoding='utf8'), open(bad_reg_file, 'w',encoding='utf8')
f1.close(), f2.close()

l = 1
# TODO здесь ваш код
with open(file, 'r', encoding='utf8') as file_for_check:
    f1, f2 = open(good_reg_file, 'a',encoding='utf8'), open(bad_reg_file, 'a',encoding='utf8')
    for line in file_for_check:
        line = line[:-1]
        #print(line)
        try:
            name, email, age = line.split(' ')
            try:
                line_checker(name, email, age)
                f1.write(f'{l:>5} Имя:{name:<15} возраст:{age:>2}  почта:{email:<30}\n')
            except Exception as exc:
                f2.write(f'{l:>5} {line} --- {exc}\n')
                print(l, line, exc)

        except ValueError:

            exc = 'неполная строка'
            print(l, line, exc)
            f2.write(f'{l:>5} {line} --- {exc}\n')




        finally:
            l += 1
    f1.close(),f2.close()
t1 = datetime.datetime.now()
print(t1-t0)