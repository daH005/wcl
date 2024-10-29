from subprocess import call


def main() -> None:
    call('cls', shell=True)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
