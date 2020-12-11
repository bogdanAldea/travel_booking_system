import docx
import re
import os
from datetime import date
from travel_booking_system.data_fields import ClientFormFields

"""
Module that pulls data from docx file
"""

# directory of docx files
CLIENT_DIRECTORY_PATH = "D:\\Coding\\Coding\\Projects\\Proiect_IT_School_v2\\travel_booking_system\\inscrieri"


def pull_raw_data(DIRECTORY_PATH, FIELDS) -> list:
    """
    Function that reads each .docx file and extracts the data
    :param DIRECTORY_PATH: dir containing all file names
    :param FIELDS:
    :return: list populated with dicts representing each file
    """
    exporting_file_data = list()
    file_names_list = os.listdir(DIRECTORY_PATH)

    # regex pattern for pulling data out
    main_regex = "(?<=:\s).+"

    # iterate over file names list
    for file_name in file_names_list:
        file_data_pull = dict()
        file_name_path = os.path.join(DIRECTORY_PATH, file_name)
        client_fields = iter(FIELDS)

        # open and read .docx file data
        docx_to_read = docx.Document(file_name_path)
        for paragraph in docx_to_read.paragraphs:
            data_value = re.findall(pattern=main_regex, string=paragraph.text)

            # ignore blank new line from docx files
            if len(data_value) > 0:

                # start forming the dictionary
                data_key = next(client_fields)
                file_data_pull[data_key] = "".join(data_value)

        exporting_file_data.append(file_data_pull)
    return exporting_file_data


"""
Client data cleaning and data conversion stage
    convert string values to int
    convert string values to date objects
    convert string values to list
"""


def convert_string_to_int(string: str, split_string=False) -> int:
    if split_string is True:
        this_string = string.split(" ")
        return int(this_string[0])
    else:
        return int(string)


def convert_string_to_date(string: str):
    split_date_string = string.split("/")
    date_object = date(day=int(split_date_string[0]), month=int(split_date_string[1]), year=int(split_date_string[2]))
    return date_object


def convert_string_to_full_date(string: str, start_field: str, end_field: str):
    split_dates = string.split(" -> ")
    date_objects = list()
    for date_string in split_dates:
        split_date_components = date_string.split("/")
        date_object = date(day=int(split_date_components[1]), month=int(split_date_components[0]), year=date.today().year)
        date_objects.append(date_object)
    client_date_data = {
        start_field: date_objects[0],
        end_field: date_objects[1]
    }
    return client_date_data


def convert_string_to_list(string: str) -> list:
    export_value_data = list()
    this_string = string.split(sep=",")
    for item in this_string:
        export_value_data.append(item.lstrip(" "))
    return export_value_data


def process_clients_data():
    raw_client_data = pull_raw_data(DIRECTORY_PATH=CLIENT_DIRECTORY_PATH, FIELDS=ClientFormFields.fields_list)

    for client_data in raw_client_data:
        for client_data_key, client_data_value in client_data.items():

            if client_data_key == ClientFormFields.NumberOfPersons:
                new_data_value = convert_string_to_int(string=client_data_value)
                client_data[client_data_key] = new_data_value

            elif client_data_key == ClientFormFields.AvailableAmount:
                new_data_value = convert_string_to_int(string=client_data_value, split_string=True)
                client_data[client_data_key] = new_data_value

            elif client_data_key == ClientFormFields.RegistrationDate:
                new_data_value = convert_string_to_date(string=client_data_value)
                client_data[client_data_key] = new_data_value

            elif client_data_key == ClientFormFields.Destinations:
                new_data_value = convert_string_to_list(string=client_data_value)
                client_data[client_data_key] = new_data_value

            elif client_data_key == ClientFormFields.Dates:
                new_data_value = convert_string_to_full_date(string=client_data_value, start_field=ClientFormFields.StartDate, end_field=ClientFormFields.EndDate)
                client_data[client_data_key] = new_data_value
    return raw_client_data


