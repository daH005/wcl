from os import remove
from os.path import isdir
from shutil import rmtree
from sys import argv


def main() -> str:
    if len(argv) < 2:
        return 'Enter at least one filename or folder.'

    if argv[1] == '-r':
        if len(argv) == 2:
            return 'Enter at least one filename or folder.'
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

    return 'Operation completed successfully.'


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
