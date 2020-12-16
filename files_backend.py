import re
import os
import docx

"""
Module that implements a file reading and data pulling function 
"""
data_pull_regex = "(?:(?<=\:\s)|(?<=\t\-\s)).+"


def pull_raw_data(DIRECTORY_PATH, FILE_EXTENSION: str) -> list:
    """
    Function reads files from DIRECTORY_PATH and pulls data in string type
    :param DIRECTORY_PATH: directory with data files
    :param FILE_EXTENSION: file extension
    :return: list of raw data
    """

    # data read from each file is appended as lists here
    export_directory_data = list()

    # get file names from directory
    file_names_list = [data_file for data_file in os.listdir(DIRECTORY_PATH) if data_file.endswith(FILE_EXTENSION)]

    # iterate over files -> open and read data
    for file_name in file_names_list:

        # set file path
        file_name_path = os.path.join(DIRECTORY_PATH, file_name)

        # each data item from each file is appended here -> a list representation of each file
        this_data_list = list()

        # check file extension and open file with its specific tool
        if FILE_EXTENSION == ".txt":
            file_to_read = open(file=file_name_path, mode="r")
            txt_content = file_to_read.readlines()
            for line in txt_content:
                this_data = re.findall(pattern=data_pull_regex, string=line)
                if len(this_data) > 0:
                    this_data_list.append("".join(this_data))

        elif FILE_EXTENSION == ".docx":
            file_to_read = docx.Document(file_name_path)
            docx_content = file_to_read.paragraphs
            for paragraph in docx_content:
                this_data = re.findall(pattern=data_pull_regex, string=paragraph.text)
                if len(this_data) > 0:
                    this_data_list.append("".join(this_data))

        export_directory_data.append(this_data_list)
    return export_directory_data