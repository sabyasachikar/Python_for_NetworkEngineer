"""
check_setup.py

Run this once you have finished the Chapter 0 setup. It confirms Python is
installed, prints the version and where it is running from, and tells you
whether your version is new enough for this course.

Run it with your virtual environment active:

    python check_setup.py
"""

import sys
import platform


def main():
    print("Python version :", platform.python_version())
    print("Operating system:", platform.system(), platform.release())
    print("Interpreter path:", sys.executable)

    major, minor = sys.version_info.major, sys.version_info.minor
    if (major, minor) >= (3, 11):
        print("Result: your Python is new enough for this course.")
    else:
        print("Result: please install Python 3.11 or later, ideally 3.14.")


if __name__ == "__main__":
    main()
