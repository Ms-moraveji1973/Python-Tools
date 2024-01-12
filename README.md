# Project Overview


In this project, we use Python to solve problems and leverage various Python tools. We utilize functionalities such as list comprehension and decorators.

#
# 1- Problems Addressed


We tackled the following set of numerical challenges:

1. The sum of the third and fifth digits equals 14.
2. The first digit is one less than twice the second digit.
3. The fourth digit is one greater than the second digit.
4. The sum of the second and third digits is 10.
5. The sum of all digits is 30.# Project Overview
#
# 2- Decorators in Python


Decorators are a powerful and flexible feature that allow you to modify or extend the behavior of functions or methods without changing their actual code. They are often used for tasks such as logging, authorization, caching, and more.

This repository provides a simple example to demonstrate the use of decorators in Python. The example involves an order processing system with decorators for checking product inventory and calculating order prices.

## Example of a Decorators
```python
def upper_case(function):
  def wrapper(*args, **kwargs):
    return function(*args, **kwargs).upper()
  return wrapper


@upper_case
def greet(name):
  return f"Hello, {name}!"


print(greet("Bard"))


