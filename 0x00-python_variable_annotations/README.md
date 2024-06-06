# 0x00. Python - Variable Annotations

## Project Information

- **Project Start Date:** June 6, 2024, 6:00 AM
- **Project End Date:** June 7, 2024, 6:00 AM
- **Checker Release Date:** June 6, 2024, 12:00 PM
- **Auto Review:** Automatically launched at the deadline

## Concepts

For this project, the following concept is expected to be understood:
- Advanced Python

## Resources

To complete this project, you may refer to:
- [Python 3 typing documentation](https://docs.python.org/3/library/typing.html)
- [MyPy cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Learning Objectives

By the end of this project, you should be able to:
1. Explain type annotations in Python 3.
2. Use type annotations to specify function signatures and variable types.
3. Understand duck typing.
4. Validate your code with `mypy`.

## Requirements

- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
  - All files should end with a new line
  - The first line of all files should be `#!/usr/bin/env python3`
  - A `README.md` file, at the root of the project folder, is mandatory
  - Code should follow the `pycodestyle` style (version 2.5)
  - All files must be executable
  - The length of your files will be tested using `wc`
  - All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - Documentation should be meaningful and describe the purpose of the module, class, or method.

## Tasks

### 0. Basic annotations - add
- **File:** `0-add.py`
- **Description:** Write a type-annotated function `add` that takes two floats `a` and `b` and returns their sum as a float.
- **Example:**
  ```python
  add(1.11, 2.22) == 1.11 + 2.22

