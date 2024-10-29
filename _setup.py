from subprocess import run
from os import mkdir, listdir
from shutil import copy
from pathlib import Path
from traceback import print_exc
import ctypes


def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as _e:
        print(_e)
        return False


def main() -> str:
    if not is_admin():
        return 'The script must be run with administrator rights.'

    commands_dir = '.\\bin\\'
    commands_filenames = listdir(commands_dir)

    commands_global_dir = '\\.wcl'
    user_home = Path.home().__str__()
    commands_global_dir_abs_path = user_home + commands_global_dir

    try:
        mkdir(commands_global_dir_abs_path)
    except FileExistsError:
        pass

    for filename in commands_filenames:
        filename = commands_dir + filename
        if '.exe' not in filename:
            continue
        copy(filename, commands_global_dir_abs_path)

    command = f'setx PATH "%PATH%;{commands_global_dir_abs_path}"'
    run(command, shell=True)

    return 'Installation completed successfully. Enjoy!'


if __name__ == '__main__':
    try:
        print(main())
    except Exception as e:
        print(e)
        print_exc()

    while True:
        pass
