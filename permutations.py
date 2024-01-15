import itertools
from copy import copy, deepcopy

from main import Character, CHARACTERS_IN_TEAPOT, receive_points, check_if_someone_got_10_lvl, add_characters_to_squad

if __name__ == '__main__':
    characters = [
        Character("Линетт", 9, 0.4146),
        Character("Шарлотта", 7, 0.9268),
        Character("Фремине", 5, 0.9146),
        Character("Дэхья", 2, 0.1951),
        Character("Мика", 8, 0.6463),
        Character("Кандакия", 7, 0.8048),
        Character("Кавех", 7, 0.6951),
        Character("Сара", 9, 0.12195),
        Character("Кэ Цин", 8, 0.8780),
        Character("Ци Ци", 8, 0.8170),
        # Character("Саю", 8, 0.6585),
        # Character("Яо Яо", 8, 0.3170),
        # Character("Джинн", 8, 0.2317),
        # Character("Фарузан", 8, 0.2073),
        # Character("Дилюк", 4, 0.7073),
        # Character("Мона", 7, 0.0976),
        # Character("Барбара", 7, 0.0121),
        # Character("Коллеи", 6, 0.3658),
        # Character("Тигнари", 5, 0.7927),
        # Character("Лини", 8, 0.8536),
        # Character("Кли", 7, 0.9390),
        # Character("Фурина", 4, 0.3659),
        # Character("Нахида", 2, 0.6951),
        # Character("Аяка", 3, 0.0731),
        # Character("Серёжа", 5, 0.2073),
        # Character("Тарталья", 5, 0.2439),
        # Character("Яэ Мико", 5, 0.4756),
        # Character("Син Цю", 7, 0.1951),
        # Character("Ёимия", 8, 0.6829),
    ]
    permutations2 = map(deepcopy, map(list, itertools.permutations(characters)))
    min_days = 10000
    optimal_permutation = []
    i = 0  # потом удалю эту переменную
    for p in permutations2:
        i += 1
        print(f"ВЫЧИСЛЯЮ ПЕРЕСТАНОВКУ {i}")
        squad = p[:CHARACTERS_IN_TEAPOT]
        waiting = p[CHARACTERS_IN_TEAPOT:]
        days = 1  # счётчик дней
        while squad:
            receive_points(squad)  # получение очков дружбы
            check_if_someone_got_10_lvl(squad)  # проверяем, если кто-то получил 10 уровень и удаляем его из отряда
            add_characters_to_squad(squad, waiting)  # добавляем персов в отряд до 8
            days += 1
        if days < min_days:
            min_days = days
            optimal_permutation = p

    print("Оптимальная перестановка персонажей: ")
    for ch in optimal_permutation:
        print(ch.name)
    print(f"В этом случае все персонажи получат 10 уровень дружбы через {min_days} дней")
