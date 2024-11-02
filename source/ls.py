from os.path import isdir
from os import listdir
from colorama import init, Fore


def main() -> None:
    init(autoreset=True)

    res = ''
    filenames = listdir()
    filenames.sort(key=lambda fn: 0 if isdir(fn) else 1)
    for filename in filenames:
        if isdir(filename):
            filename = Fore.BLUE + filename + Fore.RESET
        res += filename + ' '

    res = res.rstrip()
    if not res:
        return print('Empty folder.')
    print(res)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
