from shutil import copy
from sys import argv


def main() -> None:
    if len(argv) < 3:
        return print('Enter filename to copy and destination.')

    copy(argv[1], argv[2])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
