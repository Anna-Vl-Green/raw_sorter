from src import func

if __name__ == '__main__':
    print(func.welcome())
    directory = func.get_directory()
    user_list = func.get_string()
    func.parser_list(user_list)
    func.make_directory(directory)
    filepath_list = func.get_filepath(directory)
    unique_list = func.get_unique_list(user_list)
    transfer_list, not_found_list = func.get_transfer_list(filepath_list, unique_list)
    transfer_counter = func.copy_files(transfer_list, directory)
    func.make_report(unique_list, not_found_list, transfer_counter)
