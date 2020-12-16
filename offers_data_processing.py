import re
import os
from travel_booking_system.data_fields import OfferFormFields
from travel_booking_system import text_cleanup
from travel_booking_system.files_backend import pull_raw_data

"""
Module that pull data from offers txt files
"""

# regex patterns
date_pattern = "([0-9]+[\/]+[0-9]+)"
after_colon_pattern = "(?<=:\s).+"
rooms_pattern = "(\d+\s\w+)\sx\s(\d+\s\w+)\sx\s(\d+\s\w.+)"


def separate_data_type(RAW_DATA_LIST: list) -> tuple:
    """
    Function iterates the newly extracted data from file and separates it into 3 lists:
    - list of string data
    - list of datetime data
    - list of dict data
    :param RAW_DATA_LIST
    :return: tuple with three lists mentioned above
    """

    room_data = list()
    datetime_data = list()
    string_data = list()

    for returned_list_of_data in RAW_DATA_LIST:

        # get a list of dict formatted objects representing accommodation
        rooms_available = text_cleanup.get_rooms_object(data_list=returned_list_of_data, regex_pattern=rooms_pattern, separator=" ")
        room_data.append(rooms_available)

        # get a list of dict formatted datetime objects
        dates_available = text_cleanup.get_dates(data_list=returned_list_of_data, regex_pattern=date_pattern, separator="/", start_key="check_in", end_key="check_out")
        datetime_data.append(dates_available)

        # get a list with everything that doesn't match the rooms/dates regex pattern
        for string_item in returned_list_of_data:
            if not re.match(pattern=date_pattern, string=string_item) and not re.match(pattern=rooms_pattern, string=string_item):
                string_data.append(string_item)

    return string_data, datetime_data, room_data


def create_package_dictionary(RAW_DATA: list, STRING_OBJECTS: list, DATETIME_OBJECTS: list, ROOM_OBJECTS: list) -> list:
    """

    :param RAW_DATA:
    :param STRING_OBJECTS:
    :param DATETIME_OBJECTS:
    :param ROOM_OBJECTS:
    :return:
    """
    string_values = iter(STRING_OBJECTS)
    datetime_values = iter(DATETIME_OBJECTS)
    room_values = iter(ROOM_OBJECTS)
    list_of_packages = list()

    for X in range(len(RAW_DATA)):
        # each clean file data will be formatted as a dict here
        package_data_representation = dict()
        package_data_key = iter(OfferFormFields.fields_list)
        while True:
            try:
                KEY = next(package_data_key)

                if KEY == OfferFormFields.Dates:
                    package_data_value = next(datetime_values)

                elif KEY == OfferFormFields.Rooms:
                    package_data_value = next(room_values)

                else:
                    package_data_value = next(string_values)

                package_data_representation[KEY] = package_data_value
            except StopIteration:
                break

        list_of_packages.append(package_data_representation)
    return list_of_packages


def process_package_offers():
    """
    Function packs all above functions and return a list with clean formatted dictionaries representing all data from "oferte" files
    :return: list of dists
    """
    OFFERS_DIRECTORY_PATH = "D:\\Coding\\Coding\\Projects\\Proiect_IT_School_v2\\travel_booking_system\\oferte"
    raw_data_pull = pull_raw_data(DIRECTORY_PATH=OFFERS_DIRECTORY_PATH, FILE_EXTENSION=".txt")
    string_values, datetime_values, room_values = separate_data_type(RAW_DATA_LIST=raw_data_pull)
    return create_package_dictionary(RAW_DATA=raw_data_pull, STRING_OBJECTS=string_values, DATETIME_OBJECTS=datetime_values, ROOM_OBJECTS=room_values)



