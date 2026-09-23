from pathlib import Path

import extract_msg

from functions.file_renamer import rename_msg_file


def main():

    path = input("Enter the path to the folder containing the .msg files to rename: ")
    rename_msg_file(path)



if __name__ == "__main__":
    main()
