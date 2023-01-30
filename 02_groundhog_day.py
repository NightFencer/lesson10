# -*- coding: utf-8 -*-
from random import randint


# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
class IamGodError(Exception):

    def __str__(self):
        return 'My God mistake'

    pass


class DrankError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


ENLIGHTENMENT_CARMA_LEVEL = 777


# TODO здесь ваш код
def one_day():
    my_exception_list =[IamGodError('God'),DrankError('Drank'),CarCrashError('Car'),GluttonyError('GluttonyError'),
                        DepressionError('DepressionError'),SuicideError('Suicide')]
    dice = randint(1, 13)
    if dice < 8:
        carma = dice

    else:
        raise my_exception_list[dice-8]

    return carma


# https://goo.gl/JnsDqu
current_carma = 0
day = 1
f = open('exeptions.txt','w')
f.close()



while current_carma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        today_carma = one_day()
        current_carma += today_carma

    except Exception as exc:

        with open('exeptions.txt', 'a') as ff:
            note = f'Day - {day} {exc.args[0]} happend today--{exc}--\n'
            ff.write(note)
            print(note,end='')

        pass
    finally:
        day += 1

print(f'in {day} days surok died. Carma is {current_carma}')

# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
