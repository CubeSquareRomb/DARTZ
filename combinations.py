from funcs import sort_move

# КОМБІНАЦІЯ : (МОНЕТИ, НАЗВА КОМБ)

COMBS = {
    ## Послідовності
    'b12' : (5, 'Погана послідовність'),
    '123' : (20, 'Красива послідовність'),
    '234' : (20, 'Новачкова послідовність'),
    '345' : (25, 'Послідовність любителя'),
    '456' : (30, 'Середня послідовність'),
    '567' : (35, 'Послідовність старшого любителя'),
    '678' : (40, 'Послідовність молодшого експерта'),
    '789' : (45, 'Послідовність експерта'),
    '89a' : (200, 'Послідовність мастера'),

    ## Подвійні послідовності
    'b24': (5, 'Мінімальна подвійна послідовність'),
    '135': (10, 'Новачкова подвійна послідовність'),
    '246': (20, 'Красива послідовність любителя'),
    '357': (20, 'Середня подвійна послідовність'),
    '468': (30, 'Подвійна послідовність старшого любителя'),
    '579': (40, 'Подвійна послідовність молодшого експерта'),
    '68a': (200, 'Подвійна послідовність експерта'),

    ## Потрійні послідовності
    'b36': (10, 'Новачкова потрійна послідовність'),
    '147': (15, 'Перша потрійна послідовність'),
    '258': (30, 'Середня потрійна послідовність'),
    '369': (50, 'Красива потрійна послідовність'),
    '47a': (200, 'Потрійна послідовність рандомно-стріляючого'),

    ## Четверні послідовності
    'b48': (15, 'Мінімальна четверна послідовність'),
    '159': (40, 'Четверна послідовність рандомно-стріляючого'),
    '26a': (200, 'Четверна послідовність рандомно-стріляючого, що вибив центр'),

    ## П'ятерна послідовність
    'b5a': (200, 'Найбільша послідовність'),

    ## Квадратична послідовність
    '149': (10, 'Квадратична послідовність'),

    ## Однакові числа
    'bbb': (-1, 'Найгірший хід, зате однакові числа'),
    '111': (10, 'Однакові числа початківця І'),
    '222': (15, 'Однакові числа початківця ІІ'),
    '333': (20, 'Однакові числа початківця ІІІ'),
    '444': (25, 'Однакові числа любителя І'),
    '555': (30, 'Однакові числа любителя ІІ'),
    '666': (-100, 'Не щасливий хід'),
    '777': (40, 'Щасливий хід'),
    '888': (45, 'Однакові числа експерта'),
    '999': (75, 'Максимальний нецентральний хід'),
    'aaa': (5000, 'Звичайний хід великого дартзера'),

    ## Особливі комбінації
    'b45': (30, 'Безпечний хід'),
    '245': (35, 'Небезпечний хід'),
    '459': (40, 'Ядерний хід'),
    '577': (100, 'Тот самий 775!'),
    '228': (30, 'Агент 228'),
    'bb7': (1, 'Агент 007'),
}

def is_comb(move):
    return COMBS.get(sort_move(move), (0, 'Звичайний хід'))
