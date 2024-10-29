from sys import argv


def main() -> str:
    if len(argv) < 2:
        return 'Enter filename.'

    with open(argv[-1], 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
