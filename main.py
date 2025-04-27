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

    def __eq__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        return self.name == other.name and self.points_left == other.points_left

    def receive_points_for_teapot(self, days: int = 1):
        self.points_left -= Character.TEAPOT*days

    def receive_points_for_dailies(self, days: int = 1):
        self.points_left -= Character.DAILY*days


def receive_points(squad: list[Character], days: int = 1):
    """Получение очков дружбы персонажами в отряде. Первые 4 перса получат опыт за дейлики и чайник,
    вторые 4 перса получат опыт только за чайник."""
    for ch in squad[:CHARACTERS_FOR_DAILIES]:
        ch.receive_points_for_dailies(days)
    for ch in squad:
        ch.receive_points_for_teapot(days)


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
        Character("Вареса", 8, 0.5000),
        Character("Сиджвин", 9, 0.3171),
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
