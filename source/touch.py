from sys import argv


def main() -> str:
    if len(argv) < 2:
        return 'Enter at least one filename.'

    for filename in argv[1:]:
        with open(filename, 'w', encoding='utf-8') as f:
            pass

    return 'Operation completed successfully.'


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
