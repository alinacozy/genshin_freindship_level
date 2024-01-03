class Character:
    points_for_level = [1000, 1550, 2050, 2600, 3175, 3750, 4350, 4975, 5650]
    daily = 340  # сколько опыта дают за дейлики за 1 день
    teapot = 120  # сколько опыта дают за 24 часа в чайнике

    def __init__(self, name: str, current_level: int, progress: float):
        self.name = name  # имя перса
        points = (1 - progress) * Character.points_for_level[current_level - 1]  # сколько очков нужно для 10 уровня
        for i in range(current_level, 9):
            points += Character.points_for_level[i]
        self.points = round(points)


def recieve_points(squad):
    for i in range(min(len(squad), 4)):  # первые 4 перса получат опыт за дейлики и чайник
        squad[i].points -= (Character.daily + Character.teapot)
    for i in range(4, len(squad)):  # вторые 4 перса получат опыт только за чайник
        squad[i].points -= Character.teapot


def check_if_someone_got_10_lvl(squad):
    i = 0
    while i < len(squad):  # Проверяем весь отряд.
        # Использовала while, потому что len(squad) может меняться во время цикла
        if squad[i].points < 0:  # если кто-то достиг 10 уровня дружбы
            print(f"{squad[i].name} достигнет 10 уровня дружбы через {days} дней.")
            squad.pop(i)  # убираем перса из отряда
        i += 1


def add_characters_to_squad(squad, waiting):
    while (len(waiting) != 0) and (len(squad) < 8):  # если у нас ещё остались персонажи ожидающие помещения в отряд
        squad.append(waiting[0])  # добавляем его в отряд
        waiting.pop(0)  # удаляем из ожидающих


if __name__ == '__main__':
    characters = [
        Character("Линетт", 8, 0.6463),
        Character("Шарлотта", 6, 0.9756),
        Character("Фремине", 4, 0.5488),
        Character("Дэхья", 1, 0.1951),
        Character("Мика", 7, 0.7927),
        Character("Кандакия", 7, 0.5610),
        Character("Кавех", 7, 0.4390),
        Character("Сара", 8, 0.9146),
        Character("Кэ Цин", 8, 0.8780),
        Character("Ци Ци", 8, 0.8170),
        Character("Саю", 8, 0.6585),
        Character("Яо Яо", 8, 0.3170),
        Character("Джинн", 8, 0.2317),
        Character("Фарузан", 8, 0.2073),
        Character("Дилюк", 4, 0.7073),
        Character("Мона", 7, 0.0976),
        Character("Барбара", 7, 0.0121),
        Character("Коллеи", 6, 0.3658),
        Character("Тигнари", 5, 0.7927),
        Character("Лини", 8, 0.8536),
        Character("Кли", 7, 0.9390),
        Character("Фурина", 4, 0.2744),
        Character("Нахида", 2, 0.6951),
        Character("Аяка", 3, 0.0731),
        Character("Серёжа", 5, 0.2073),
        Character("Тарталья", 5, 0.2439),
        Character("Яэ Мико", 5, 0.4756),
        Character("Син Цю", 7, 0.1951),
        Character("Ёимия", 8, 0.6341),
    ]
    squad = characters[:8]
    waiting = characters[8:]
    days = 1  # счётчик дней
    while len(squad) != 0:
        recieve_points(squad)  # получение очков дружбы
        check_if_someone_got_10_lvl(squad)  # проверяем, если кто-то получил 10 уровень и удаляем его из отряда
        add_characters_to_squad(squad, waiting)  # добавляем персов в отряд до 8
        days += 1
