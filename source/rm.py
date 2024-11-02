from os import remove
from os.path import isdir
from shutil import rmtree
from sys import argv


def main() -> None:
    if len(argv) < 2:
        return print('Enter at least one filename or folder.')

    if argv[1] == '-r':
        if len(argv) == 2:
            return print('Enter at least one filename or folder.')
        r = True
        start_index = 2
    else:
        r = False
        start_index = 1

    for filename in argv[start_index:]:
        if isdir(filename):
            if r:
                rmtree(filename)
        else:
            remove(filename)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
