import datetime


def generate_filename():
    # To make each generated file unique, use the date and time of writing the file
    timestamp = datetime.datetime.now()
    year = timestamp.year
    month = timestamp.month
    day = timestamp.day
    hour = timestamp.hour
    minute = timestamp.minute
    second = timestamp.second

    filename = "lap times " + month + '-' + day + '-' + year + ' ' + hour + ':' + minute + ':' + second + ".txt"

    return filename


def open_file(filename):
    # Open the file for writing and return the object to write to the file
    lap_data_file = open(filename, "w")
    return lap_data_file


def close_file(file_obj):
    # Close the file after the writing is completed
    file_obj.close()


def write_lap_data_to_file(lap_data_list):
    # Write the recorded lap data to a file

    # Open the file for writing
    lap_data_file = open_file(generate_filename())

    # INSERT CODE TO WRITE TO FILE

    # Close the file after writing
    close_file(lap_data_file)
