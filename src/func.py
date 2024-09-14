import os
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
        if char.isalnum() or char == '_':
            name += char.lower()
        else:
            if name:
                selected_files.append(name)
                name = ''
    if name:
        selected_files.append(name)
    return selected_files


def make_directory(current_dir):
    """
    Функция создаёт новую папку директории, с которой ведётся работа.
    :param current_dir: Путь к директории в формате строки.
    """
    current_dir += '/selected'
    makedirs(current_dir, exist_ok=True)


def get_filepath(current_dir):
    """
    Функция запускает рекурсивный поиск файлов внутри рабочей директории и записывает их имена вместе с расширениями
    в список.
    :param current_dir: Путь к директории в формате строки.
    :return: list: Список файлов с расширениями.
    """
    listing_files: list = []
    for file in scandir(current_dir):
        if file.is_file():
            listing_files.append(file)
    listing_filenames = [file.name for file in listing_files]
    return listing_filenames


def get_unique_list(new_list):
    """
    Функция исключает дубликаты в полученном списке.
    :param new_list: Список имён файлов.
    :return: list: Фильтрованный список.
    """
    return list(set(new_list))


def get_transfer_list(listing_files, selected_files):
    """
    Функция формирует список выбранных и список отсутствующих файлов.
    :param listing_files: list: Список файлов в рабочей директории.
    :param selected_files: list: Список файлов, выбранных пользователем.
    :return: list: Список выбранных имён файлов с расширениями.
    :return: list: Список не найденных имён файлов с расширениями.
    """
    transfer_list_files: list = []
    transfer_not_found: list = []
    for name in selected_files:
        found = False
        for i, filename in enumerate(listing_files):
            if name.lower() in filename.lower():
                transfer_list_files.append(filename)
                del listing_files[i]
                found = True
                break
        if not found:
            transfer_not_found.append(name)
    return transfer_list_files, transfer_not_found


def copy_files(transfer_list, parent_dir, new_dir):
    """
    Функция копирования файлов.
    :param transfer_list: Список файлов для копирования.
    :param parent_dir: str: Путь к рабочей директории в формате строки.
    :param new_dir: str: Путь к директории, в которую нужно скопировать файлы.
    :return: int: Количество скопированных файлов.
    """
    counter = 0
    for filename in transfer_list:
        source = os.path.join(parent_dir, filename)
        purpose = os.path.join(new_dir, filename)
        copy2(str(source), str(purpose))
        counter += 1
    return counter


def make_report(transfer_list, not_found_list, counter):
    """
    Функция возвращает сообщение об окончании процедуры копирования файлов.
    :param transfer_list: list: Список файлов для копирования.
    :param not_found_list: Список отсутствующих файлов.
    :param counter: int: Счётчик скопированных файлов.
    :return: str: Строка с сообщением для пользователя.
    """
    return (f'Копирование выбранных файлов закончено. Выбрано {len(transfer_list)} файлов. '
            f'Скопировано {counter} файлов.\n'
            f'Не найдено {len(not_found_list)}: {', '.join(not_found_list)}')
