# Python

We rely on [Fourmat](https://github.com/4Catalyzer/fourmat) to automatically format and lint code according to our style guidelines. Below are additional guidelines that are not taken care of by Fourmat.

## Data types

Prefer immutable data types over their mutable equivalents. Specifically, prefer `tuple` and `frozenset` over `list` and `set` respectively when the relevant collections will not be mutated. However, it is acceptable to use `list` over `tuple` for collections that semantically constitute homogeneous lists rather than heterogeneous tuples, though `tuple` may still be better when the list is short.

## Import styles

If a module defines a homogeneous collection of items (e.g. `models`, `views` or `layers`), prefer importing the module over the individual items from that module.

```python
# Yes
from . import views
# No
from .views import FooView, BarView
```

## Test layout

Unit tests for a module should be placed under a `test/` subdirectory of the package containing the module, and should be named as the module file, prepended with `test_`.

```
my_package/my_module.py
my_package/test/test_my_module.py
```

Functional tests should be placed under a top-level `tests/` directory. Their file names should start with `test_`.

```
my_package/my_module.py
tests/test_functionality.py
```

## Section dividers

It is acceptable to use the following section divider when it aids clarity. For example, this section divider can be useful after imports or between groups of related functions.

```python
# -----------------------------------------------------------------------------
```

## Preferred tools

- For linting and formatting, use [fourmat](https://github.com/4Catalyzer/fourmat).
- For data frame manipulation, use [pandas](https://pandas.pydata.org/).
- For building command line interfaces, prefer [Click](http://click.pocoo.org/).
- For testing, use [pytest](https://pytest.org/).
    - Prefer [fixtures](https://docs.pytest.org/en/latest/fixture.html) over explicit setup and teardown.
