from os import getcwd


def main() -> None:
    print(getcwd())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
