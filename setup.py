import cx_Freeze
import sys


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("job_application_interface.py", base=base, icon="clienticon.ico")]

cx_Freeze.setup(
    name = "Job Application Interface",
    options = {"build_exe": {"packages":["tkinter","pathlib", "pandas", "datetime", "time"], "include_files":["clienticon.ico"]}},
    version = "0.01",
    description = "Job Application GUI",
    executables = executables
    )