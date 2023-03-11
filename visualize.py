import argparse
from datetime import datetime
import sys
import plotext as plt



def parse_arguments(args):
    try:
        parser = argparse.ArgumentParser(
            description='Visualize Data within a time frame', prog='visualize')
        parser.add_argument('-s', '--start-date', required=True,
                            help='Start date. Date format: DD-MM-YYYY', type=date)
        parser.add_argument('-e', '--end-date', required=True,
                            help='End date. Date format: DD-MM-YYYY', type=date)

        parsed_arg = parser.parse_args(args)
        return parsed_arg
    except argparse.ArgumentError as err:
        sys.exit(err)
    except argparse.ArgumentTypeError as err:
        sys.exit(err)


def date(date_string):
    return datetime.strptime(date_string, '%d-%m-%Y').date()


def get_coordinates(args):
    x_values = []
    y_values = []

    api_data = {
        "01-01-2022": 300,
        "02-01-2022": 500,
        "03-01-2022": 700,
        "04-01-2022": 1300,
        "05-01-2022": 2000,
        "06-01-2022": 3000,
        "07-01-2022": 3500,
        "08-01-2022": 4000,
        "09-01-2022": 4500,
        "10-01-2022": 5000,
        "11-01-2022": 20000,
        "12-01-2022": 35000,
        "13-01-2022": 46000,
        "14-01-2022": 70000,
        "15-01-2022": 90000
    }

    start_date = args.start_date
    end_date = args.end_date

    if start_date.strftime('%d-%m-%Y') in api_data and end_date.strftime('%d-%m-%Y') in api_data:
        for key, value in api_data.items():
            if date(key) >= start_date and date(key) <= end_date:
                # print(key, value)
                x_values.append(date(key))
                y_values.append(value)
    elif start_date.strftime('%d-%m-%Y') not in api_data:
        sys.exit("Given start date is not available")
    elif end_date.strftime('%d-%m-%Y') not in api_data:
        sys.exit("Given end date is not available")
    else:
        sys.exit("An error occurred. Please check your input")

    coordinates = {
        "X": x_values,
        "Y": y_values
    }
    return coordinates


def visualize_data(data):
    # data = get_data(args)

    plt.date_form('d/m/Y')
    plt.title("Userbase Growth Graph")
    plt.ylabel("Number of Users")
    plt.xlabel("Dates")
    no_of_users = data.get("Y")
    dates = plt.datetimes_to_string(data.get("X"))

    plt.bar(dates, no_of_users)
    plt.yticks(no_of_users)

    plt.show()



args =  parse_arguments(sys.argv[1:])
coordinates = get_coordinates(args)
visualize_data(coordinates)
