from cx_Freeze import setup, Executable
import os

# Path to your logo image
logo_path = os.path.join(os.getcwd(), 'logo.png')

# Additional files to include
files = [logo_path]

# Setup configuration
setup(
    name="PasswordManager",
    version="0.1",
    description="A simple password manager",
    executables=[Executable("main.py", base="Win32GUI")],
    options={
        "build_exe": {
            "packages": ["tkinter", "pyperclip"],
            "include_files": files,
        }
    }
)
