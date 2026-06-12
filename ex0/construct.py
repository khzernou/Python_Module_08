#!/usr/bin/env python3

import os
import sys
import site


def is_virtua_env() -> bool:
    """returns true if we are in venv"""
    return sys.prefix != sys.base_prefix


def get_site_packages() -> str:
    """return active site-package path or sends msg"""
    paths = site.getsitepackages()
    return paths[0] if paths else "unknown"


def print_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print(f"Global package installation path:\n{get_site_packages()}\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate     # On Windows\n")
    print("Then run this program again.")


def print_inside_matrix() -> None:
    """display status when venv is active"""
    venv_path = sys.prefix
    venv_name = os.path.basename(os.path.normpath(venv_path))

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print(f"Package installation path:\n{get_site_packages()}")


def main() -> None:
    if is_virtua_env():
        print_inside_matrix()
    else:
        print_outside_matrix()


if __name__ == "__main__":
    main()
