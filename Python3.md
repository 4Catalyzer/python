# Python 3 Guide
_Python 3 features for Python 2 developers._

## Class definitions

Python 3 no longer has old-style classes. Class definitions no longer need to explicitly extend `object`.

```python
class MyClass:
    pass


# Equivalent to:
class MyClass(object):
    pass
```

## `super`

Python 3 permits [`super`](https://docs.python.org/3/library/functions.html#super) to omit its arguments.

```python
class MyChildClass(MyParentClass):
    def method(self, arg):
        super().method(arg)

        # Equivalent to:
        super(MyChildClass, self).method(arg)
```

## Iterable unpacking

Python 3 supports using `*` to unpack iterables.

```python
head, *rest = seq
seq = (a, *b, c)

# Equivalent to:
head, rest = seq[0], seq[1:]
seq = (a,) + tuple(b) + (c,)
```

Python 3 also supports using `**` to unpack dictionaries.

```python
my_dict = {
    **dict_1,
    'foo': 1,
    'bar': 2,
    **dict_2,
}

# Equivalent to:
my_dict = {}
my_dict.update(dict_1)
my_dict['foo'] = 1
my_dict['bar'] = 2
my_dict.update(dict_2)
```
