from os import getcwd


def main() -> str:
    return getcwd()


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
