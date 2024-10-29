import PyInstaller.__main__
from os import listdir

if __name__ == '__main__':
    commands_dir = '.\\source\\'
    filenames = listdir(commands_dir)

    for filename in filenames:
        PyInstaller.__main__.run([
            commands_dir + filename,
            '--onefile',
            '--distpath=.\\bin',
            '--specpath=.\\bin\\cache',
            '--workpath=.\\bin\\cache',
        ])

        PyInstaller.__main__.run([
            '_setup.py',
            '--onefile',
            '--distpath=.\\',
            '--specpath=.\\bin\\cache',
            '--workpath=.\\bin\\cache',
        ])
