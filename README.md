# 4Catalyzer Python Style Guide
_An utterly unreasonable Python style guide, mostly for trolling purposes._

Use [PEP 8](https://www.python.org/dev/peps/pep-0008/), with the following additions.

## Exceptions

This guide is intended to present general guidelines. Most modules should follow this style guide. However, specific modules should freely disregard specific guidelines whenever necessary.

## Python 3

Whenever possible, projects should use the newest release of Python 3.

## Multi-line constructs

Indent continuation lines by the standard 4 spaces. Always use trailing commas whenever legal (note that this differs between Python 2 and Python 3). Match the indentation of the closing bracket with the indentation of the start of the multi-line construct.

```python
# Tuple:
my_tuple = (
    foo,
    bar,
    baz,
)

# List:
my_list = [
    foo,
    bar,
    baz,
]

# Dictionary:
my_dict = {
    'foo': foo,
    'bar': bar,
    'baz': baz,
}

# Function signature:
def my_func(
    foo,
    bar,
    baz,
):
    pass

# Function call:
my_func(
    foo,
    bar,
    baz,
)

# Function call with nested multiline construct:
my_func(
    foo,
    (
        bar,
        baz,
        qux,
    ),
)
```

When this syntax is not possible, indent by 8 spaces.

```python
# Multiple with statement:
with \
        context_manager_1(
            foo,
            bar,
            baz,
        ), \
        context_manager_2(
            foo,
            bar,
            baz,
        ):
    pass
```

Prefer to either put all elements on a single line, or have one element per line, except when grouping is especially semantically meaningful.

```python
# Good:
my_tuple = (
    foo,
    bar,
    baz,
)

# Good:
my_tuple = (
    foo, bar, baz,
)

# Usually bad:
my_tuple = (
    foo, bar,
    baz,
)
```

If a function takes two arguments, where the second argument is a collection, it is acceptable to use a multiline construct for only that second argument.

```python
my_func(foo, (
    bar,
    baz,
    qux,
))
```

As noted in PEP 8, prefer implicit line continuation inside brackets over explicit continuations with backslashes.

```python
# Good:
from foo import (
    bar, baz, qux,
)

# Bad:
from foo import \
    bar, baz, qux
```

## Data types

Prefer immutable data types over their mutable equivalents. Specifically, prefer `tuple` and `frozenset` over `list` and `set` respectively when the relevant collections will not be mutated. However, it is acceptable to use `list` over `tuple` for collections that semantically constitute homogeneous lists rather than heterogeneous tuples, though `tuple` may still be better when the list is short.

## Preferred tools

- For data frame manipulation, use [pandas](https://pandas.pydata.org/).
- For building command line interfaces, prefer [Click](http://click.pocoo.org/).
- For testing, use [pytest](https://pytest.org/).
  - Prefer [fixtures](https://docs.pytest.org/en/latest/fixture.html) over explicit setup and teardown.

## Section dividers

It is acceptable to use the following section divider when it aids clarity. For example, this section divider can be useful after imports or between groups of related functions.

```python
# -----------------------------------------------------------------------------
```

## Unit tests

Modules and functions should be unit tested inside a separate module using the following name / path convention:

```bash
my_module.py
tests/test_my_module.py
```

The unit tests themselves should be written using pytest by convention.

