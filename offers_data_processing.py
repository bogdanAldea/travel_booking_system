import re
import os
from travel_booking_system.data_fields import OfferFormFields
from travel_booking_system import text_cleanup

"""
Module that pull data from offers txt files
"""

# regex patterns
date_pattern = "([0-9]+[\/]+[0-9]+)"
after_colon_pattern = "(?<=:\s).+"
rooms_pattern = "(?<=\t\-\s)(\d\s\w+)\sx\s(\d\s\w+)\sx\s(\d+\s\w.+)"

# directory of offers txt files
OFFERS_DIRECTORY_PATH = "D:\\Coding\\Coding\\Projects\\Proiect_IT_School_v2\\travel_booking_system\\oferte"


def pull_partial_offers_data(DIRECTORY_PATH):
    """
    :param DIRECTORY_PATH:
    :param FIELDS:
    :return:
    """
    exporting_file_data = list()

    # get files only with .txt extension
    offers_data_files = [data_file for data_file in os.listdir(OFFERS_DIRECTORY_PATH) if data_file.endswith(".txt")]

    # iterate over filenames list
    for file_name in offers_data_files:
        file_name_path = os.path.join(DIRECTORY_PATH, file_name)
        data_to_read = open(file=file_name_path, mode="r")
        exporting_file_data.append(data_to_read.readlines())
    return exporting_file_data


def pull_full_data(PARTIAL_DATA):
    """

    :param PARTIAL_DATA:
    :return:
    """
    export_full_data_list = list()
    for partial_data_list in PARTIAL_DATA:
        new_data_list = list()
        list_of_dates = list()
        list_of_rooms = list()

        for data_item_string in partial_data_list:
            if re.search(pattern=after_colon_pattern, string=data_item_string):
                new_data_list.append("".join(re.findall(pattern=after_colon_pattern, string=data_item_string)))

            elif re.search(pattern=date_pattern, string=data_item_string):
                list_of_dates.append(re.findall(pattern=date_pattern, string=data_item_string))

            elif re.search(pattern=rooms_pattern, string=data_item_string):
                result = re.findall(pattern=rooms_pattern, string=data_item_string)
                for result_item in result:
                    list_of_rooms.append(list(result_item))

        new_data_list.insert(2, list_of_dates)
        new_data_list.append(list_of_rooms)
        export_full_data_list.append(new_data_list)
    return export_full_data_list


def convert_to_date(DATE_VALUES):
    """

    :param DATE_VALUES:
    :return:
    """
    date_objects_list = list()
    for string_list in DATE_VALUES:
        date_dict = text_cleanup.get_date_object(raw_param_data=string_list, separator="/", start_key="Start", end_key="End")
        date_objects_list.append(date_dict)
    return date_objects_list


def process_offers_data(OFFERS_FULL_DATA):
    """

    :param OFFERS_FULL_DATA:
    :return:
    """
    file_data_list = list()
    for data_item in OFFERS_FULL_DATA:
        data_dictionary_object = dict()
        data_key = iter(OfferFormFields.fields_list)
        data_value = iter(data_item)
        counter = 0

        while counter != len(data_item):
            key = next(data_key)
            value = next(data_value)

            if key == OfferFormFields.MinNumberOfPersons or key == OfferFormFields.MaxNumberOfPersons:
                data_dictionary_object[key] = int(value)

            elif key == OfferFormFields.Dates:
                clean_value = convert_to_date(DATE_VALUES=value)
                data_dictionary_object[key] = clean_value

            elif key == OfferFormFields.Rooms:
                clean_value = text_cleanup.get_room_object(raw_param_data=value, separator=" ")
                data_dictionary_object[key] = clean_value

            else:
                data_dictionary_object[key] = value
            counter += 1
        file_data_list.append(data_dictionary_object)
    return file_data_list


# if __name__ == '__main__':
#     partial_data = pull_partial_offers_data(DIRECTORY_PATH=OFFERS_DIRECTORY_PATH)
#     full_data = pull_full_data(PARTIAL_DATA=partial_data)
#     result = process_offers_data(OFFERS_FULL_DATA=full_data)
#     for item in result:
#         print(item)







