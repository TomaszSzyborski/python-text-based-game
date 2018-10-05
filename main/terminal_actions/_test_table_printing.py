if __name__ == '__main__':
    from main.terminal_actions.printing import _read_csv, print_as_texttable, print_as_prettytable, print_as_tabulate

    headers, values = _read_csv("_test_file_for_table_printing.csv")
    print("TABULATE LIBRARY:\n")
    print("With table format None")
    print_as_tabulate(headers, values)
    print("\n", 40*"#", "\n")
    print("With table format 'orgtbl'")
    print_as_tabulate(headers, values, "orgtbl")
    print("\n", 80*"=", "\n")

    print("PRETTYTABLE LIBRARY:\n")
    print_as_prettytable(headers, values)
    print("\n", 80*"=", "\n")

    print("TEXTTABLE LIBRARY:\n")
    print_as_texttable(headers, values)
    print("\n", 80*"=", "\n")
