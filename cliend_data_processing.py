import docx
import re
import os
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




