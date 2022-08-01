import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\berktug\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\berktug\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("giris.py", base=base, icon="ateshotelicon.ico")]


cx_Freeze.setup(
    name = "Ateş Otel Yönetim Sistemi",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["ateshotelicon.ico",'tcl86t.dll','tk86t.dll', 'resimler','database']}},
    version = "1.0",
    description = "Ateş Otel Yönetim Sistemi | Berktuğ Berke Ateş",
    executables = executables
    )
