CHARACTERS_IN_TEAPOT = 8
CHARACTERS_FOR_DAILIES = 4


class Character:
    POINTS_FOR_LEVEL = (
        1000, 1550, 2050, 2600, 3175, 3750, 4350, 4975,
        5650)  # Количество опыта дружбы, нужное для перехода на сл. уровень
    DAILY = 340  # сколько опыта дают за дейлики за 1 день
    TEAPOT = 120  # сколько опыта дают за 24 часа в чайнике

    @staticmethod
    def points_for_10_level(current_level: int, progress: float) -> int:
        """Сколько очков нужно для 10 уровня"""
        points = (1 - progress) * Character.POINTS_FOR_LEVEL[current_level - 1]
        points += sum(Character.POINTS_FOR_LEVEL[current_level:])
        return round(points)

    def __init__(self, name: str, current_level: int, progress: float):
        self.name = name  # имя перса
        self.points_left = Character.points_for_10_level(current_level, progress)  # сколько очков нужно до 10 уровня

    def receive_points_for_teapot(self):
        self.points_left -= Character.TEAPOT

    def receive_points_for_dailies(self):
        self.points_left -= Character.DAILY


def receive_points(squad: list[Character]):
    """Получение очков дружбы персонажами в отряде. Первые 4 перса получат опыт за дейлики и чайник,
    вторые 4 перса получат опыт только за чайник."""
    for ch in squad[:CHARACTERS_FOR_DAILIES]:
        ch.receive_points_for_dailies()
    for ch in squad:
        ch.receive_points_for_teapot()


def check_if_someone_got_10_lvl(squad: list[Character]) -> list[Character]:
    """Проверяем, получил ли кто-то из персонажей 10 уровень дружбы. Если да, удаляем этого перса из отряда
    и добавляем его в массив (чтобы потом вывести сообщение)"""
    i = 0
    result = []  # массив, который возвращает функция
    while i < len(squad):  # Проверяем весь отряд.
        # Использовала while, потому что len(squad) может меняться во время цикла
        if squad[i].points_left < 0:  # если кто-то достиг 10 уровня дружбы
            result.append(squad[i])
            squad.pop(i)  # убираем перса из отряда
        else:
            i += 1
    return result


def message_of_10_lvls(chs: list[Character], days: int):
    for ch in chs:
        print(f"{ch.name} достигнет 10 уровня дружбы через {days} дней.")


def add_characters_to_squad(squad: list[Character], waiting: list[Character]):
    """Добавляем в отряд персонажей "из ожидания" чтобы персонажей в отряде стало 8"""
    while waiting and (
            len(squad) < CHARACTERS_IN_TEAPOT):  # если у нас ещё остались персонажи ожидающие помещения в отряд
        squad.append(waiting[0])  # добавляем его в отряд
        waiting.pop(0)  # удаляем из ожидающих


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
        Character("Фурина", 4, 0.3659),
        Character("Нахида", 2, 0.6951),
        Character("Аяка", 3, 0.0731),
        Character("Серёжа", 5, 0.2073),
        Character("Тарталья", 5, 0.2439),
        Character("Яэ Мико", 5, 0.4756),
        Character("Син Цю", 7, 0.1951),
        Character("Ёимия", 8, 0.6829),
    ]
    squad = characters[:CHARACTERS_IN_TEAPOT]
    waiting = characters[CHARACTERS_IN_TEAPOT:]
    days = 1  # счётчик дней
    while squad:
        receive_points(squad)  # получение очков дружбы
        # проверяем, если кто-то получил 10 уровень и удаляем его из отряда:
        characters_with_10_lvl = check_if_someone_got_10_lvl(squad)
        # выводим сообщение о том, какие персонажи получили 10 уровень дружбы:
        message_of_10_lvls(characters_with_10_lvl, days)
        add_characters_to_squad(squad, waiting)  # добавляем персов в отряд до 8
        days += 1
