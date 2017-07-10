# Python 3 Guide
_Python 3 for Python 2 devs._

## Super calls

Whenever possible, projects should take advantage of Python 3 features and syntax. For example prefer [new style super calls](https://docs.python.org/3.5/library/functions.html#super) to old stlye.

Prefer this:
```python
super().method()
```

to this:
```python
super(klass, self).method()
```
