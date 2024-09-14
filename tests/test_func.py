import pytest
import tempfile
import os
from src import func
from tests.test_config import (test_user_string, test_user_list, test_listing_filenames, test_new_list,
                               test_new_list_files, test_not_found)


@pytest.fixture(scope='module')
def generate_files():
    """
    Создаёт набор файлов для тестирования.
    """
    os.chdir('./test_dir/test_files')
    for i in range(0, 10):
        filename = f'DSC_10{i}.txt'
        with open(filename, 'w') as f:
            f.write('')


def test_welcome():
    """
    Тестирует функцию welcome().
    :return: str
    """
    assert func.welcome() == 'Добро пожаловать в "RAW sorter"!'


def test_get_directory(monkeypatch):
    """
    Тестирует функцию get_directory().
    :param monkeypatch:
    :return: str
    """
    monkeypatch.setattr('builtins.input', lambda _: "directory")
    assert func.get_directory() == "directory"


def test_get_string(monkeypatch):
    """
    Тестирует функцию get_string().
    :return: str
    """
    monkeypatch.setattr('builtins.input', lambda _: "users_string")
    assert func.get_string() == "users_string"


def test_parser_list():
    """
    Тестирует функцию parser_list().
    :param new_string: str
    :return: list
    """
    assert func.parser_list(test_user_string) == test_user_list


def test_make_directory():
    """
    Тестирует функцию make_directory().
    :param current_dir: str
    """
    func.make_directory('./test_dir')
    os.chdir('./test_dir')
    assert os.path.isdir('selected')
    os.rmdir('selected')


def test_make_directory_if_exist():
    """
    Тестирует функцию make_directory().
    :param current_dir: str
    """
    func.make_directory('./test_dir/test_files')
    os.chdir('./test_dir/test_files')
    assert os.path.isdir('selected')


def test_get_filepath(generate_files):
    """
    Тестирует функцию get_filepath().
    :param current_dir: str
    :return: list
    """
    assert func.get_filepath('.') == test_listing_filenames


def test_get_unique_list():
    """
    Тестирует функцию get_unique_list().
    :param new_list: list
    :return: list
    """
    set_1 = set(func.get_unique_list(test_new_list))
    set_2 = set(test_user_list)
    assert set_1 - set_2 == set()


def test_transfer_list(generate_files):
    """
    Тестирует функцию transfer_list().
    :param listing_files: list
    :param selected_files: list
    :return: list
    :return: list
    """
    pass


def test_copy_files(names_list, parent_dir, new_dir):
    """
    Тестирует функцию copy_files().
    :param names_list: list
    :param parent_dir: str
    :param new_dir: str
    :return: int
    """
    pass


def test_make_report(names_list, not_found_list, counter):
    """
    Тестирует функцию make_report().
    :param names_list: list
    :param not_found_list: list
    :param counter: int
    :return: str
    """
    pass
