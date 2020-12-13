from datetime import date


def get_date_from_string(string: str, separator: str):
    split_date_string = string.split(sep=separator)
    date_object = date(day=int(split_date_string[0]), month=int(split_date_string[1]), year=int(split_date_string[2]))
    return date_object


def get_date_object(raw_param_data: list, separator: str, start_key: str, end_key: str) -> dict:
    list_of_objects = list()
    for string in raw_param_data:
        split_string = string.split(sep=separator)
        default_year = date.today().year
        if len(split_string) == 3:
            default_year = int(split_string[2])
        date_object = date(day=int(split_string[0]), month=int(split_string[1]), year=default_year)
        list_of_objects.append(date_object)
    DICT = {
        start_key: list_of_objects[0],
        end_key: list_of_objects[1]
    }
    return DICT


def get_room_object(raw_param_data: list, separator: str) -> list:
    """

    :param raw_param_data:
    :param separator:
    :return:
    """
    list_of_objects = list()
    for inner_data_list in raw_param_data:
        room_data_dictionary = dict()
        for raw_data in inner_data_list:
            clean_data = raw_data.split(sep=separator)
            room_data_dictionary[clean_data[1].capitalize()] = int(clean_data[0])
        list_of_objects.append(room_data_dictionary)
    return list_of_objects


def get_int_object(string: str, split_string=False) -> int:
    if split_string is True:
        this_string = string.split(" ")
        return int(this_string[0])
    else:
        return int(string)


def get_list_object(string: str) -> list:
    export_value_data = list()
    this_string = string.split(sep=",")
    for item in this_string:
        export_value_data.append(item.lstrip(" "))
    return export_value_data




