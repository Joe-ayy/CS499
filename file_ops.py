import datetime
import sys

def generate_filename():
    # To make each generated file unique, use the date and time of writing the file
    timestamp = datetime.datetime.now()
    year = timestamp.year
    month = timestamp.month
    day = timestamp.day
    hour = timestamp.hour
    minute = timestamp.minute
    second = timestamp.second

    filename = "lap_times_" + str(month) + '-' + str(day) + '-' + str(year) + '-' + str(hour) + '-' + str(minute) + '-' + str(second) + ".txt"

    return filename


def open_file(filename):
    # Open the file for writing and return the object to write to the file
    try:
        lap_data_file = open(filename, "a")
    except ValueError:
        print("Error opening file. Exiting.")
        sys.exit(1)
    return lap_data_file

def close_file(file_obj):
    # Close the file after the writing is completed
    file_obj.close()

def write_lap_data_to_file(lap_data_list, line):
    # Write a line of recorded lap data to a file
    lap_data_file = open_file(lap_data_list)

    # Write the line of data to the file
    lap_data_file.write(line)

    close_file(lap_data_file)
