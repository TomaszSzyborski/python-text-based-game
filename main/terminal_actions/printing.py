import os
import sys
import time

import csv

import texttable
import tabulate
import prettytable

from main.user_actions.actions_descriptions_dictfile import actions_descriptions


def _clear_screen_before_output():
    """
    Clears terminal window output before printing
    new strings like user actions, states or pieces of dialogue
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_actions():
    _clear_screen_before_output()
    for k, v in actions_descriptions.items():
        print(f"{k:<20} => {v:<20}")


def slow_typing(words, t=0.125):
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(t)

    sys.stdout.write("\n")
    sys.stdout.flush()


def _read_csv(file_name):
    """
    Reads csv file
    and returns a tuple of headers and list of rows of values

    (string) -> (tuple)
    :param file_name:
    :return headers, values:
    """
    with open(file_name, "r") as csv_file:
        contents = list(csv.reader(csv_file, delimiter=","))
        headers = contents[0]
        rows_of_values = contents[1:]
        return headers, rows_of_values


def print_as_tabulate(headers, rows_of_values, table_format=None):
    """
    Prints collection of headers and values using tabulate library

    (headers, values) -> None
    :param table_format: example usage - none, orgtbl
    :param headers: collection of headers
    :param rows_of_values: list of rows of values to print
    :return:
    """
    print(tabulate.tabulate(rows_of_values, headers=headers, tablefmt=table_format))


def print_as_prettytable(headers, rows_of_values):
    """
    Prints collection of headers and values using tabulate library

    (headers, values) -> None
    :param headers: collection of headers
    :param rows_of_values: list of rows of values to print
    :return:
    """
    table = prettytable.PrettyTable(headers)
    for row in rows_of_values:
        table.add_row(row)

    print(table)


def print_as_texttable(headers, rows_of_values):
    """
    Prints collection of headers and values using tabulate library

    (headers, values) -> None
    :param headers: collection of headers
    :param rows_of_values: list of rows of values to print
    :return:
    """
    table = texttable.Texttable()
    # table.set_deco(texttable.Texttable.HEADER)
    # table.add_rows(header=headers, rows=rows_of_values)
    data = rows_of_values.insert(0, headers)
    table.add_rows(rows_of_values)
    print(table.draw())
