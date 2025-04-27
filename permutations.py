import itertools
import math
from copy import copy, deepcopy

from main import Character, CHARACTERS_FOR_DAILIES, CHARACTERS_IN_TEAPOT, receive_points, check_if_someone_got_10_lvl, add_characters_to_squad

if __name__ == '__main__':
    characters = [
        Character("Иансан", 6, 0.1220),
        Character("Оророн", 6, 0.7073),
        Character("Серёжа", 9, 0.1098),
        Character("Райден", 9, 0.2805),
        Character("Син Цю", 9, 0.5975),
        Character("Ризли", 8, 0.0122),
        Character("Арлекино", 8, 0.7561),
        Character("Нахида", 8, 0.1585),
        Character("Яэ Мико", 8, 0.8658),
        Character("Яо Яо", 8, 0.8293),
        Character("Мавуика", 8, 0.6707),
        Character("Качина", 9, 0.6220),
        # Character("Вареса", 8, 0.5000),
        # Character("Сиджвин", 9, 0.3171),
    ]

    min_days = math.inf
    max_days = 0
    optimal_permutation = []
    worst_permutation = []
    i = 0  # сколько перестановок уже выполнено, просто чтобы отслеживать, как работает программа
    length_percent = math.factorial(len(characters)) / 2400
    #за счет того что используем комбинации по 4, количество перестановок уменьшается в 24 раза, а еще делим на 100 чтобы считать в процентах
    print(length_percent)

    combinations_of_first_4=map(copy, map(list, itertools.combinations(characters, 4)))
    for combination in combinations_of_first_4:
        characters_copy=characters.copy()
        for character in combination:
            characters_copy.remove(character)
        permutations2 = map(deepcopy, map(list, itertools.permutations(characters_copy)))
        for permutation in permutations2:
            current_permutation = deepcopy(combination) + permutation

            i += 1 # номер перестановки
            print(f"Выполнено работы: {i / length_percent}%")

            squad = current_permutation[:CHARACTERS_IN_TEAPOT]
            waiting = current_permutation[CHARACTERS_IN_TEAPOT:]
            days = 1  # счётчик дней
            while squad:
                receive_points(squad)  # получение очков дружбы
                check_if_someone_got_10_lvl(squad)  # проверяем, если кто-то получил 10 уровень и удаляем его из отряда
                add_characters_to_squad(squad, waiting)  # добавляем персов в отряд до 8
                days += 1
            if days < min_days:
                min_days = days
                optimal_permutation = current_permutation
            if days > max_days:
                max_days = days
                worst_permutation = current_permutation

    print("Оптимальная перестановка персонажей: ")
    for ch in optimal_permutation:
        print(ch.name)
    print(f"В этом случае все персонажи получат 10 уровень дружбы через {min_days} дней")

    print("Самая неоптимальная перестановка персонажей: ")
    for ch in worst_permutation:
        print(ch.name)
    print(f"В этом случае все персонажи получат 10 уровень дружбы через {max_days} дней")
