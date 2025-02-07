from sys import argv


def main() -> None:
    if len(argv) < 2:
        return print('Enter the filename.')

    with open(argv[-1], 'r', encoding='utf-8') as f:
        return print(f.read())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
