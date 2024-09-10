from shutil import copy2
from os import scandir, makedirs


def welcome():
    """
    Функция приветствует пользователя.
    :return: str: Строка приветствия.
    """
    return 'Добро пожаловать в "RAW sorter"!'


def get_directory():
    """
    Функция запрашивает путь к директории для работы с файлами в ней и возвращает этот путь в виде строки.
    :return: str: Путь к директории для работы.
    """
    directory: str = input("Введите адрес директории с файлами, которые нужно скопировать для дальнейшей работы:\n")
    return directory


def get_string():
    """
    Функция запрашивает у пользователя список файлов для копирования и возвращает его в виде строки.
    :return: str: Строка с именами файлов, заданных пользователем.
    """
    raw_string: str = input("Введите список файлов, которые нужно обработать:\n")
    return raw_string


def parser_list(new_string: str):
    """
    Функция анализирует строку и создаёт на её основе список имён файлов без расширений. Все символы в нижнем регистре.
    :param new_string: Строка, содёржащая имена файлов для дальнейшей работы с ними.
    :return: list: Строка с базовыми именами файлов (без указания расширения).
    """
    name: str = ''
    selected_files: list = []
    for char in new_string:
        if char.isalnum or char == '_':
            name.join(char.lower())
        else:
            selected_files.append(name)
    return selected_files


def make_directory(current_dir):
    """
    Функция создаёт новую папку директории, с которой ведётся работа.
    :param current_dir: Путь к директории в формате строки.
    """
    current_dir += '/selected'
    makedirs(current_dir, exist_ok=False)


def get_filepath(current_dir):
    """
    Функция запускает рекурсивный поиск файлов внутри рабочей директории и записывает их имена вместе с расширениями
    в список.
    :param current_dir: Путь к директории в формате строки.
    :return: list: Список файлов с расширениями.
    """
    listing_files: list = []
    for file in scandir(current_dir):
        listing_files.append(file)
    return listing_files


def get_unique_list(new_list):
    """
    Функция исключает дубликаты в полученном списке.
    :param new_list: Список имён файлов.
    :return: list: Фильтрованный список.
    """
    return list(set(new_list))


def transfer_list(listing_files, selected_files):
    """
    Функция формирует список выбранных и список отсутствующих файлов.
    :param listing_files: Список файлов в рабочей директории.
    :param selected_files: Список файлов, выбранных пользователем.
    :return: list: Список выбранных имён файлов с расширениями.
    :return: list: Список не найденных имён файлов с расширениями.
    """
    new_list_files: list = []
    not_found: list = []
    for name in selected_files:
        for filename in listing_files:
            if name.lower() in filename.lower():
                new_list_files.append(listing_files.pop(filename))
                break
        else:
            not_found.append(name)
    return new_list_files, not_found


def copy_files(names_list, parent_dir, new_dir):
    """
    Функция копирования файлов
    :param names_list: Список файлов для копирования.
    :param parent_dir: str: Путь к рабочей директории в формате строки.
    :param new_dir: str: Путь к директории, в которую нужно скопировать файлы.
    :return: int: Количество скопированных файлов.
    """
    counter = 0
    for filename in names_list:
        source = parent_dir + filename
        purpose = new_dir + filename
        copy2(source, purpose)
        counter += 1
    return counter


def make_report(names_list, not_found_list, counter):
    """
    Функция возвращает сообщение об окончании процедуры копирования файлов.
    :param names_list: list: Список файлов для копирования.
    :param not_found_list: Список отсутствующих файлов.
    :param counter: int: Счётчик скопированных файлов.
    :return: str: Строка с сообщением для пользователя.
    """
    return (f'Копирование выбранных файлов закончено. Выбрано {len(names_list)} файлов. Скопировано {counter} файлов.\n'
            f'Не найдено {len(not_found_list)}: {', '.join(not_found_list)}')
