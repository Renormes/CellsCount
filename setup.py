import sys
from cx_Freeze import setup, Executable
import sys


sys.setrecursionlimit(9000)

build_exe_options = {"packages": ["os", "ultralytics", "pillow", "pandas", "concurrent", "openpyxl", "cv2", "shutil"], "includes": ["tkinter"]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="CounterCells",
    version="0.1",
    description="Contador de células",
    options={"build_exe": build_exe_options},
    executables=[Executable("soul.py", base=base)]
)