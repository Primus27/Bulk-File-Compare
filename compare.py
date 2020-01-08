"""
Title: Bulk compare files in two directories with the same name
Author: Primus27
"""

import os
from pathlib import Path, PurePath
import argparse
from datetime import datetime
try:
    from termcolor import colored as colour
except ImportError:
    print("'termcolor' module is missing.")
    exit()

current_version = 1.0


def scan_file(file1, file2):
    """
    Scans two files and compares discrepancies.
    :param file1: A file to compare.
    :param file2: Another file to compare.
    :return: Boolean value on whether the files have the same contents.
    """
    command = f"cmp -s \"{file1}\" \"{file2}\"; echo $?"
    results = os.popen(command).read()

    if results == "0":
        return True
    else:
        return False


def enum_files(folder_path):
    """
    Enumerates files in a path.
    :param folder_path: Root folder path for enumeration.
    :return: List containing all files in a folder.
    """
    # List of all files in path
    f_list = []
    # Enumerate files
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            # Generate the absolute/relative path for each file
            file_path = str(Path(os.path.join(root, file))).replace("\\ ", "")
            f_list.append(file_path)
    # No files found
    if len(f_list) == 0:
        print(colour("[*] No files found in specified directory\n", "red"))

    return f_list


def main():
    """
    Main method
    """
    # Output current time of scan
    print(colour(f"[*] Scan started: {datetime.now()}\n", "green"))

    # Enumerate files in path
    file_list1 = enum_files(path1)
    file_list2 = enum_files(path2)

    path1_count = len(file_list1)
    path2_count = len(file_list2)
    match_count = 0
    non_match_count = 0
    file_found_count = 0
    total_iterate_count = 0

    print(colour(f"[*] Number of files in path 1: {path1_count}", "yellow"))
    print(colour(f"[*] Number of files in path 2: {path2_count}", "yellow"))
    print()

    for file1 in file_list1:
        file_found = False
        filename1 = PurePath(file1).name

        for file2 in file_list2:
            filename2 = PurePath(file2).name

            if filename1 == filename2:
                file_found = True
                diff_check = scan_file(file1, file2)

                print(f"Filename: {filename1}")
                message = f"Match: {diff_check}"

                if diff_check:
                    print(colour(message, "green"))
                    match_count += 1
                else:
                    print(colour(message, "red"))
                    non_match_count += 1

                print(f"Path1: {file1}")
                print(f"Path1: {file2}")
                print()
        if show_not_found and not file_found:
            print(f"Filename: {file1}")
            print(colour("File not found in path 2", "yellow"))

        if file_found:
            file_found_count += 1

        total_iterate_count += 1

    # Output comparison of scanned files to total files
    col_code = "yellow" if total_iterate_count == path1_count else "red"
    print(colour(f"[*] {total_iterate_count}/{path1_count} Files scanned",
                 col_code))

    col_code = "yellow" if file_found_count == path1_count else "red"
    print(colour(f"[*] Files with the same name found: "
                 f"{file_found_count}/{path1_count}", col_code))

    col_code = "yellow" if match_count == (match_count + non_match_count) \
        else "red"
    print(colour(f"[*] Content matches found: "
                 f"{match_count}/{match_count + non_match_count}", col_code))


if __name__ == '__main__':
    # Define argument parser
    parser = argparse.ArgumentParser()

    # Remove existing action groups
    parser._action_groups.pop()

    # Create a required and optional group
    required = parser.add_argument_group("required arguments")
    optional = parser.add_argument_group("optional arguments")

    # Define arguments
    required.add_argument("-p1", "--path1", action="store", dest="path1",
                          help="Main path (absolute or relative). This is the "
                               "path which you want every file checked.",
                          required=True)
    required.add_argument("-p2", "--path2", action="store", dest="path2",
                          help="Sub path (absolute or relative). This is the "
                               "path where files may be skipped if they are "
                               "not in path1.",
                          required=True)
    optional.add_argument("-o", "--toOutput", action="store_true",
                          dest="output_friendly",
                          help="Removes ANSI escape sequences for terminal "
                               "colouring. It is useful for redirecting.")
    optional.add_argument("-s", "--silent", action="store_false",
                          dest="show_not_found",
                          help="If a file in path1 is not found in path2, "
                               "hide in output.")
    optional.add_argument("--version", action="version",
                          version=f"%(prog)s {current_version}",
                          help="Display program version.")
    args = parser.parse_args()

    # Args
    path1 = Path(args.path1)
    path2 = Path(args.path2)
    output_friendly = args.output_friendly
    show_not_found = args.show_not_found

    if output_friendly:
        def colour(message, tc_colour):
            """
            Overwrites the termcolor "color" function so that the output
            features no escape sequences (for colour). This means it can be
            output to a file without the escape sequences
            :param message: Message for print statement
            :param tc_colour: Colour otherwise for termcolor
            :return: Message that was input
            """
            return message

    # Main method
    main()
