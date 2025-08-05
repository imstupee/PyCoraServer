import os
import shutil
import subprocess
from pathlib import Path

PROJECT_NAME = "PyCoraServer"
ENTRY_POINT_FILE = "main.py"
OUTPUT_DIR_NAME = "dist"

def clean_old():
    print("Removing old files...")
    for folder in [OUTPUT_DIR_NAME, "build"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)

def build_exe():
    print("Starting PyInstaller...")

    args = [
        'pyinstaller',
        #'--windowed',
        '--onefile',
        '--noconfirm',
        '--name', PROJECT_NAME,
        '--distpath', OUTPUT_DIR_NAME,
        ENTRY_POINT_FILE
    ]

    subprocess.run(args, check=True)


def main():
    clean_old()
    build_exe()
    print(f"Build ready! EXE-file in folder {OUTPUT_DIR_NAME}")

if __name__ == "__main__":
    main()