# 0x01. Python - Async

## Python - Back-end
**Weight:** 1  
**Project Start:** Jun 10, 2024 6:00 AM  
**Project End:** Jun 11, 2024 6:00 AM  
**Checker Release:** Jun 10, 2024 12:00 PM  
**Auto Review:** Launched at the deadline  

## Resources
Read or watch:
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
By the end of this project, you should be able to:
- Explain the `async` and `await` syntax
- Execute an async program with `asyncio`
- Run concurrent coroutines
- Create `asyncio` tasks
- Use the `random` module

## Requirements
- A `README.md` file at the root of the project is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- All your files must be executable
- The length of your files will be tested using `wc`
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5.x)
- All your functions and coroutines must be type-annotated
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Tasks

### Task 0: The basics of async
Write an asynchronous coroutine that takes an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (inclusive and float value) seconds and eventually returns it.

Use the `random` module.

#### Example:
```python
# 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

