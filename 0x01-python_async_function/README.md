# Python Async

This repository contains solutions for tasks related to asynchronous programming in Python.

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [The basics of async](#the-basics-of-async)
  - [Let's execute multiple coroutines at the same time with async](#lets-execute-multiple-coroutines-at-the-same-time-with-async)
  - [Measure the runtime](#measure-the-runtime)
  - [Tasks](#tasks-1)
  - [Tasks](#tasks-2)
- [Copyright](#copyright)

## Description

This project focuses on understanding and implementing asynchronous programming in Python using `async` and `await` syntax along with the `asyncio` library. It covers concepts like executing async programs, running concurrent coroutines, creating asyncio tasks, and utilizing modules like `random`.

## Learning Objectives

By completing this project, you'll be able to:

- Explain `async` and `await` syntax in Python.
- Execute async programs with `asyncio`.
- Run concurrent coroutines.
- Create asyncio tasks.
- Utilize the `random` module effectively.

## Requirements

- All code is written and tested on Ubuntu 18.04 LTS using Python 3.7.
- All files must be executable and adhere to the specified style guidelines.
- Use type annotations for functions and coroutines.
- Provide documentation for modules and functions.
- Ensure that the length and execution of files meet specified criteria.
- Use `#!/usr/bin/env python3` as the first line in all files.
- Use `pycodestyle` for code style enforcement.

## Tasks

### The basics of async

Write an asynchronous coroutine `wait_random` that waits for a random delay between 0 and a given `max_delay` (default: 10 seconds) and returns it.

```python
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

### Let's execute multiple coroutines at the same time with async

Write an async routine `wait_n` that spawns `wait_random` `n` times with a specified `max_delay`, returning the list of delays in ascending order without using `sort()` due to concurrency.

```python
#!/usr/bin/env python3

import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

### Measure the runtime

Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

```python
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
```

### Tasks

Write a function `task_wait_random` that takes an integer `max_delay` and returns an asyncio.Task.

```python
#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

### Tasks

Alter the code from `wait_n` into a new function `task_wait_n`, where `task_wait_random` is being called.

```python
#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

## Copyright

© 2024 ALX, All rights reserved.
