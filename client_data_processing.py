import docx
import re
import os
from datetime import date
from travel_booking_system.files_backend import pull_raw_data
from travel_booking_system.data_fields import ClientFormFields
from travel_booking_system import text_cleanup


"""
Module that pulls data from clients docx file
"""

# directory of docx files
CLIENT_DIRECTORY_PATH = "D:\\Coding\\Coding\\Projects\\Proiect_IT_School_v2\\travel_booking_system\\inscrieri"


def process_client_data(RAW_DATA) -> list:
    """
    Function takes pulled client data and client form fields and assigns them to each other with converted data
    :param RAW_DATA: list of data
    :return: list of dictionaries
    """
    export_clients_data = list()
    for client_data in RAW_DATA:
        client_data_representation = dict()
        client_data_key = iter(ClientFormFields.fields_list)
        client_data_value = iter(client_data)
        while True:
            try:
                data_field = next(client_data_key)
                data_item = next(client_data_value)

                if data_field == ClientFormFields.NumberOfPersons:
                    data_item = int(data_item)

                elif data_field == ClientFormFields.AvailableAmount:
                    split_string = data_item.split(" ")
                    data_item = int(split_string[0])

                elif data_field == ClientFormFields.RegistrationDate:
                    split_string = data_item.split("/")
                    data_item = date(day=int(split_string[0]), month=int(split_string[1]), year=int(split_string[2]))

                elif data_field == ClientFormFields.Dates:
                    split_item_data = data_item.split(" -> ")
                    data_item = text_cleanup.get_date_object(raw_param_data=split_item_data, separator="/", start_key="check_in", end_key="check_out")

                elif data_field == ClientFormFields.Destinations:
                    data_item = text_cleanup.get_list_object(string=data_item)

                client_data_representation[data_field] = data_item
            except StopIteration:
                break
        export_clients_data.append(client_data_representation)
    return export_clients_data

