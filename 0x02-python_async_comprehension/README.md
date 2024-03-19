# Python - Async Comprehension

This repository contains Python code related to asynchronous comprehension. The tasks involve writing coroutines, utilizing async comprehensions, and measuring runtime for parallel comprehensions.

## Learning Objectives

By completing the tasks in this project, you will learn:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Resources

To better understand the concepts and techniques covered in this project, you may find the following resources helpful:

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- What’s New in Python: Asynchronous Comprehensions / Generators
- Type-hints for generators

## Tasks Overview

### Task 0: Async Generator

Write a coroutine called `async_generator` that loops 10 times, asynchronously waits for 1 second each time, and yields a random number between 0 and 10 using the `random` module.

### Task 1: Async Comprehensions

Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over the `async_generator` coroutine.

### Task 2: Run Time for Four Parallel Comprehensions

Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather` and measures the total runtime.

## Requirements

- All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- Code should adhere to PEP 8 style guidelines
- Documentation is mandatory for modules and functions
- Type annotations are required for functions and coroutines

## Repository Structure

The repository structure is as follows:

- **GitHub repository:** [alx-backend-python](https://github.com/yourusername/alx-backend-python)
- **Directory:** 0x02-python_async_comprehension

## Files

- **0-async_generator.py**: Contains the implementation of the async generator coroutine for Task 0.
- **1-async_comprehension.py**: Implements the async comprehension coroutine for Task 1.
- **2-measure_runtime.py**: Implements the measure_runtime coroutine for Task 2.

## Usage

To run the scripts for each task, execute the corresponding main files provided:

- **0-main.py**: For Task 0
- **1-main.py**: For Task 1
- **2-main.py**: For Task 2

Example usage:

```
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
```

## Conclusion

Completing these tasks will enhance your understanding of asynchronous programming in Python and improve your ability to write efficient and concise code using async comprehensions and generators.

---

Copyright © 2024 ALX. All rights reserved.
