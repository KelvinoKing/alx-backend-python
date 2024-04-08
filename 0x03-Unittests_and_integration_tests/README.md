# 0x03. Unittests and Integration Tests

This repository contains the solutions for the tasks related to unit tests and integration tests as part of the ALX Backend Python curriculum.

## Overview

This project focuses on developing unit tests and integration tests for various functions and classes using the `unittest` framework in Python. The tasks involve writing tests to ensure the correctness of functions, mocking HTTP requests, parameterizing tests, and testing integration between different parts of the code.

## Learning Objectives

By completing this project, you will be able to:

- Understand the difference between unit tests and integration tests.
- Implement common testing patterns such as mocking, parametrizations, and fixtures.
- Write comprehensive test cases to ensure code reliability and correctness.

## Requirements

- All code is interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files must end with a newline.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should adhere to the `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules, classes, and functions should have appropriate documentation.
- Functions and coroutines must be type-annotated.

## Files and Directories

- `utils.py`: Utility functions for testing.
- `client.py`: Contains classes for interacting with external APIs.
- `fixtures.py`: Fixtures used for integration testing.
- `test_utils.py`: Unit tests for utility functions.
- `test_client.py`: Unit and integration tests for client classes.

## Tasks

1. **Parameterize a unit test**: Write unit tests for `utils.access_nested_map` function.
2. **Parameterize a unit test (exception)**: Test exception handling in `utils.access_nested_map`.
3. **Mock HTTP calls**: Test `utils.get_json` function by mocking HTTP requests.
4. **Parameterize and patch**: Test memoization decorator by patching methods.
5. **Mocking a property**: Unit test for mocking properties in `GithubOrgClient`.
6. **More patching**: Test `GithubOrgClient.public_repos` method using patching.
7. **Parameterize**: Unit test for `GithubOrgClient.has_license` method with parametrization.
8. **Integration test: fixtures**: Integration test for `GithubOrgClient.public_repos` method using fixtures.

## Execution

To execute the tests, run:

```bash
$ python -m unittest discover tests
```

Ensure all tests pass before submitting the code.

For detailed instructions on each task, refer to the corresponding file in the repository.

## Author

This repository is maintained by Kelvin Njoroge Gachihi. Contact kelvinoking@outlook.com for inquiries.

Feel free to contribute or report issues by creating a pull request or opening an issue in the repository. Happy coding!
