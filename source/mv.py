from shutil import move
from sys import argv


def main() -> str:
    if len(argv) < 3:
        return 'Enter filename to move and destination.'

    move(argv[1], argv[2])
    return 'Operation completed successfully.'


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
