# Python

We rely on [Fourmat](https://github.com/4Catalyzer/fourmat) to automatically format and lint code according to our style guidelines. Below are additional guidelines that are not taken care of by Fourmat.

## Data types

Prefer immutable data types over their mutable equivalents. Specifically, prefer `tuple` and `frozenset` over `list` and `set` respectively when the relevant collections will not be mutated. However, it is acceptable to use `list` over `tuple` for collections that semantically constitute homogeneous lists rather than heterogeneous tuples, though `tuple` may still be better when the list is short.

## Preferred tools

- For linting and formatting, use [fourmat](https://github.com/4Catalyzer/fourmat).
- For data frame manipulation, use [pandas](https://pandas.pydata.org/).
- For building command line interfaces, prefer [Click](http://click.pocoo.org/).
- For testing, use [pytest](https://pytest.org/).
    - Prefer [fixtures](https://docs.pytest.org/en/latest/fixture.html) over explicit setup and teardown.
