from os.path import isdir
from os import listdir

BLUE = '\033[94m'
RESET = '\033[0m'


def main() -> None:

    res = ''
    filenames = listdir()
    filenames.sort(key=lambda fn: 0 if isdir(fn) else 1)
    for filename in filenames:
        if isdir(filename):
            filename = BLUE + filename + RESET
        res += filename + ' '

    res = res.rstrip()
    if not res:
        return print('The folder is empty.')
    print(res)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
