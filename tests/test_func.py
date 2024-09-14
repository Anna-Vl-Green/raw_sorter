import shutil
import pytest
import os
from src import func
from tests.test_config import (test_user_string, test_user_parsing_list, test_user_list, test_listing_filenames,
                               test_new_list, test_transfer_list_files, test_transfer_not_found, test_counter,
                               test_report)


@pytest.mark.xfail(raises=FileNotFoundError)
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
    """
    assert func.parser_list(test_user_string) == test_user_parsing_list


def test_make_directory():
    """
    Тестирует функцию make_directory().
    """
    func.make_directory('./test_dir')
    os.chdir('./test_dir')
    assert os.path.isdir('selected')
    os.rmdir('selected')


def test_make_directory_if_exist():
    """
    Тестирует функцию make_directory().
    """
    func.make_directory('./test_dir/test_files')
    os.chdir('./test_dir/test_files')
    assert os.path.isdir('selected')


@pytest.mark.xfail(raises=FileNotFoundError)
def test_get_filepath(generate_files):
    """
    Тестирует функцию get_filepath().
    :return: list
    """
    assert func.get_filepath('.') == test_listing_filenames


def test_get_unique_list():
    """
    Тестирует функцию get_unique_list().
    :return: list
    """
    set_1 = set(func.get_unique_list(test_new_list))
    set_2 = set(test_user_list)
    assert set_1 - set_2 == set()


@pytest.mark.xfail(raises=FileNotFoundError)
def test_transfer_list(generate_files):
    """
    Тестирует функцию transfer_list().
    :return: list
    :return: list
    """
    listing_files = func.get_filepath('.')
    transfer_list_files, transfer_not_found = func.get_transfer_list(listing_files, test_user_list)
    assert transfer_list_files == test_transfer_list_files
    assert transfer_not_found == test_transfer_not_found


@pytest.mark.xfail(raises=FileNotFoundError)
def test_copy_files(generate_files):
    """
    Тестирует функцию copy_files().
    :return: int
    """
    counter = func.copy_files(test_transfer_list_files, '.', './selected')
    assert counter == test_counter
    for name in test_transfer_list_files:
        assert os.path.isfile(name)
        shutil.rmtree('./selected')
        os.mkdir('./selected')


def test_make_report():
    """
    Тестирует функцию make_report().
    :return: str
    """
    report = func.make_report(test_user_list, test_transfer_not_found, test_counter)
    assert report == test_report
