from sys import argv


def main() -> None:
    if len(argv) < 2:
        return print('Enter at least one filename.')

    for filename in argv[1:]:
        with open(filename, 'w', encoding='utf-8') as f:
            pass


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
