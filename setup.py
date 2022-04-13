import cx_Freeze
import sys


base=None

if sys.platform == 'win32':
    base="Win32GUI"

executables=[cx_Freeze.Executable("covidgui.py",base=base,icon="Corona.ico")]

cx_Freeze.setup(
    name="Christine-Client",
    options={"build.exe": {"packages":{"tkinter","pygame","win10toast_click","requests","webbrowser"},"include_files":{"Corona.ico"}}},
    version="0.1",
    description= "test",
    executables=executables)
