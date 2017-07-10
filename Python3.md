# Python 3 Guide
_Python 3 for Python 2 devs._

## Super calls

Prefer [new style super calls](https://docs.python.org/3/library/functions.html#super) to old style.

Prefer this:
```python
super().method()
```

to this:
```python
super(MyClass, self).method()
```
