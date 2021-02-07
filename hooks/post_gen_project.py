import os

library_or_application = '{{ cookiecutter.library_or_application }}'

if library_or_application != "Library":
    os.remove("setup.py")
