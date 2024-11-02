from shutil import move
from sys import argv


def main() -> None:
    if len(argv) < 3:
        return print('Enter filename to move and destination.')

    move(argv[1], argv[2])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
