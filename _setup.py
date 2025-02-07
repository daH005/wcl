from subprocess import run
from os import mkdir, listdir
from shutil import copy
from pathlib import Path
from traceback import print_exc


def main() -> None:
    commands_dir = '.\\source\\'
    commands_filenames = listdir(commands_dir)

    commands_global_dir = '\\.wcl'
    user_home = Path.home().__str__()
    commands_global_dir_abs_path = user_home + commands_global_dir

    try:
        mkdir(commands_global_dir_abs_path)
    except FileExistsError:
        pass

    for filename in commands_filenames:
        if '.py' not in filename:
            continue

        py_filename = commands_dir + filename
        copy(py_filename, commands_global_dir_abs_path)

        cmd_filename = filename.replace('.py', '.cmd')
        with open(commands_global_dir_abs_path + '\\' + cmd_filename, 'w', encoding='utf-8') as f:
            f.write(f'@echo off\npy %~dp0{filename} %*')

    command = f'setx PATH "%PATH%;{commands_global_dir_abs_path}"'
    run(command, shell=True)

    print('The installation has been completed successfully. Enjoy!')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        print_exc()

    while True:
        pass
