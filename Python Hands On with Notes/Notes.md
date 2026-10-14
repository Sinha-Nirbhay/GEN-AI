<hr style="border: 2px solid">

<span style="font-size: 2em"><b>Data Structures in Python</b></span>

Python has **basic data types** (single values) and **data structures** (collections that hold multiple values).

***Basic data types***

| Type | Example | Notes |
|---|---|---|
| `int` | `10`, `-5` | Non Decimal Integer **OR** +ve , -ve Whole Number, no size limit |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `bool` | `True`, `False` | Subclass of `int` (`True == 1`, `False == 0`) Eg :- 2 + True = 3 , 2 + False = 2 |
| `str` | `"hello"` | Sequence of characters, **immutable** |

***Data structures (collections)***

| Type | Example | Ordered | Mutable | Duplicates |
|---|---|---|---|---|
| `list` | `[1, 2, 3]` | Yes | Yes | Allowed |
| `tuple` | `(1, 2, 3)` | Yes | No | Allowed |
| `set` | `{1, 2, 3}` | No | Yes | Not allowed |
| `dict` | `{"a": 1, "b": 2}` | Yes (insertion order) | Yes | Keys unique |

- **list** — ordered, changeable collection; access by index (`lst[0]`).
- **tuple** — ordered, unchangeable collection; faster than a list and can be used as a dict key.
- **set** — unordered collection of unique items; fast membership check (`x in s`).
- **dict** — stores `key: value` pairs; access by key (`d["a"]`).


<hr style="border: 2px solid">

<span style="font-size: 2em"><b>List</b></span>

A **list** is an ordered, mutable collection that can hold multiple items of any data type. It is created using square brackets `[]` or the `list()` constructor.

***Features of list***

- **Ordered** — items keep the position in which they were added.
- **Mutable** — items can be added, removed, or changed after creation.
- **Allows duplicates** — the same value can appear more than once.
- **Heterogeneous** — can hold different data types together (int, str, bool, list, tuple, dict, etc.).
- **Indexed** — supports positive indexing (starts at `0`) and negative indexing (starts at `-1` from the end).
- **Dynamic size** — grows and shrinks as items are added or removed.
- **Supports slicing** — `lst[start:stop:step]` returns a new list.
- **Can be nested** — a list can contain other lists (2D lists).

***List methods***

| Method | Input | Return | Affects Original List |
|---|---|---|---|
| `append(x)` | One item | `None` | Yes |
| `insert(i, x)` | Index, item | `None` | Yes |
| `extend(iterable)` | Any iterable (list, tuple, set, str) | `None` | Yes |
| `remove(x)` | Value | `None` (`ValueError` if value not found) | Yes |
| `pop(i)` | Optional index (default is last) | The removed item (`IndexError` if list is empty) | Yes |
| `clear()` | Nothing | `None` | Yes |
| `index(x)` | Value | Index of first match (`ValueError` if not found) | No |
| `count(x)` | Value | Number of occurrences | No |
| `sort(key, reverse)` | Optional `key`, optional `reverse` | `None` | Yes |
| `reverse()` | Nothing | `None` | Yes |
| `copy()` | Nothing | New list (shallow copy) | No |

***Operations***

| Operation | Input | Return | Affects Original List |
|---|---|---|---|
| `lst += other` | Any iterable | Same list, extended | Yes |
| `del lst[i]` | Index or slice | Nothing (it is a statement) | Yes |
| `lst[i] = x` | Index, new value | Nothing | Yes |
| `lst[a:b] = iterable` | Slice, iterable | Nothing | Yes |
| `lst[a:b:c]` | Start, stop, step | New list | No |
| `lst + other` | Another list | New list | No |
| `lst * n` | Integer | New list | No |
| `x in lst` | Value | `True` / `False` | No |

***Built-in functions on list***

| Function | Input | Return | Affects Original List |
|---|---|---|---|
| `len(lst)` | List | Number of items | No |
| `sum(lst)` | List of numbers | Total of all items | No |
| `min(lst)` | List | Smallest item | No |
| `max(lst)` | List | Largest item | No |
| `any(lst)` | List | `True` if at least one item is truthy | No |
| `all(lst)` | List | `True` if all items are truthy | No |
| `sorted(lst)` | List, optional `key`, `reverse` | New sorted list | No |
| `reversed(lst)` | List | Reverse iterator (use `list()` to see it) | No |

***Key points***

- `sort()` changes the original list and returns `None`, whereas `sorted()` returns a new list.
- `b = a` does not copy the list, both names point to the same list. Use `copy()` or `a[:]` for a copy.
- `append()` adds one item as it is, `extend()` adds each item of an iterable separately.
- `remove()` works by value, `pop()` and `del` work by index, and only `pop()` returns the removed item.

<hr style="border: 2px solid">

<span style="font-size: 2em"><b>Set</b></span>

A **set** is an unordered collection of **unique** items. It is created using curly braces `{}` or the `set()` constructor. An empty set must be created with `set()`, because `{}` creates an empty dictionary.

***Features of set***

- **Unordered** — no fixed position, so indexing and slicing are not supported.
- **Unique items** — duplicates are removed automatically.
- **Mutable** — items can be added or removed after creation.
- **Items must be hashable** — only immutable items (int, str, tuple) are allowed, not list, set, or dict.
- **Fast membership check** — `x in s` is quicker than in a list.
- **Supports mathematical operations** — union, intersection, difference, symmetric difference.
- **Heterogeneous** — can hold different data types together.
- **Dynamic size** — grows and shrinks as items are added or removed.
- `frozenset` is the immutable version of a set.

***Set methods***

| Method | Input | Return | Affects Original Set |
|---|---|---|---|
| `add(x)` | One item | `None` | Yes |
| `update(*iterables)` | One or more iterables | `None` | Yes |
| `remove(x)` | Value | `None` (`KeyError` if value not found) | Yes |
| `discard(x)` | Value | `None` (no error if value not found) | Yes |
| `pop()` | Nothing | A random removed item (`KeyError` if set is empty) | Yes |
| `clear()` | Nothing | `None` | Yes |
| `copy()` | Nothing | New set (shallow copy) | No |
| `union(*others)` | One or more iterables | New set with all items | No |
| `intersection(*others)` | One or more iterables | New set with common items | No |
| `difference(other)` | Iterable | New set with items only in the first set | No |
| `symmetric_difference(other)` | Iterable | New set with items in either set but not both | No |
| `intersection_update(*others)` | One or more iterables | `None` | Yes |
| `difference_update(*others)` | One or more iterables | `None` | Yes |
| `symmetric_difference_update(other)` | Iterable | `None` | Yes |
| `issubset(other)` | Iterable | `True` / `False` | No |
| `issuperset(other)` | Iterable | `True` / `False` | No |
| `isdisjoint(other)` | Iterable | `True` if no common items | No |

***Operations***

| Operation | Input | Return | Affects Original Set |
|---|---|---|---|
| `a \| b` | Another set | New set (union) | No |
| `a & b` | Another set | New set (intersection) | No |
| `a - b` | Another set | New set (difference) | No |
| `a ^ b` | Another set | New set (symmetric difference) | No |
| `a \|= b`, `a &= b`, `a -= b`, `a ^= b` | Another set | Same set, updated | Yes |
| `a <= b` / `a >= b` | Another set | `True` / `False` (subset / superset) | No |
| `x in s` | Value | `True` / `False` | No |

***Built-in functions on set***

| Function | Input | Return | Affects Original Set |
|---|---|---|---|
| `len(s)` | Set | Number of items | No |
| `sum(s)` | Set of numbers | Total of all items | No |
| `min(s)` | Set | Smallest item | No |
| `max(s)` | Set | Largest item | No |
| `any(s)` | Set | `True` if at least one item is truthy | No |
| `all(s)` | Set | `True` if all items are truthy | No |
| `sorted(s)` | Set, optional `key`, `reverse` | New sorted **list** | No |
| `set(iterable)` | Any iterable | New set (removes duplicates) | No |

***Key points***

- `remove()` raises an error if the item is missing, `discard()` does not.
- `pop()` removes an arbitrary item, since a set has no order.
- `set(my_list)` is a quick way to remove duplicates, but the original order is not guaranteed.
- `sorted(s)` returns a list, not a set.

<hr style="border: 2px solid">

<span style="font-size: 2em"><b>Tuple</b></span>

A **tuple** is an ordered, **immutable** collection that can hold multiple items of any data type. It is created using parentheses `()` or the `tuple()` constructor. A single-item tuple needs a trailing comma, for example `(1,)`.

***Features of tuple***

- **Ordered** — items keep the position in which they were added.
- **Immutable** — items cannot be added, removed, or changed after creation.
- **Allows duplicates** — the same value can appear more than once.
- **Heterogeneous** — can hold different data types together.
- **Indexed** — supports positive and negative indexing, and slicing.
- **Faster and uses less memory than a list** — because it cannot change.
- **Hashable** — can be used as a dictionary key or set item (if all its items are hashable).
- **Supports packing and unpacking** — `a, b = (1, 2)`.
- **Can be nested** — a mutable item inside a tuple (like a list) can still be changed.

***Tuple methods***

| Method | Input | Return | Affects Original Tuple |
|---|---|---|---|
| `count(x)` | Value | Number of occurrences | No |
| `index(x)` | Value, optional start and stop | Index of first match (`ValueError` if not found) | No |

A tuple has only these two methods, because it is immutable.

***Operations***

| Operation | Input | Return | Affects Original Tuple |
|---|---|---|---|
| `t[i]` | Index | Item at that index | No |
| `t[a:b:c]` | Start, stop, step | New tuple | No |
| `t + other` | Another tuple | New tuple | No |
| `t * n` | Integer | New tuple | No |
| `x in t` | Value | `True` / `False` | No |
| `a, b = t` | Tuple | Unpacks items into variables | No |
| `first, *rest = t` | Tuple | Unpacks first item and the remaining as a list | No |
| `t[i] = x` | Index, new value | `TypeError` (not allowed) | No |
| `del t[i]` | Index | `TypeError` (not allowed) | No |

***Built-in functions on tuple***

| Function | Input | Return | Affects Original Tuple |
|---|---|---|---|
| `len(t)` | Tuple | Number of items | No |
| `sum(t)` | Tuple of numbers | Total of all items | No |
| `min(t)` | Tuple | Smallest item | No |
| `max(t)` | Tuple | Largest item | No |
| `any(t)` | Tuple | `True` if at least one item is truthy | No |
| `all(t)` | Tuple | `True` if all items are truthy | No |
| `sorted(t)` | Tuple, optional `key`, `reverse` | New sorted **list** | No |
| `reversed(t)` | Tuple | Reverse iterator (use `tuple()` to see it) | No |
| `tuple(iterable)` | Any iterable | New tuple | No |

***Key points***

- To "change" a tuple, convert it to a list, modify it, and convert it back.
- `sorted(t)` returns a list, not a tuple.
- `(1)` is an int, `(1,)` is a tuple.
- Use a tuple for fixed data (coordinates, days of the week), and a list for data that changes.

<hr style="border: 2px solid">

<span style="font-size: 2em"><b>Dictionary</b></span>

A **dictionary** is a collection of **key-value pairs**. It is created using curly braces `{key: value}` or the `dict()` constructor. Each key is used to access its value.

***Features of dictionary***

- **Key-value pairs** — data is stored as `key: value` and accessed by key, not by index.
- **Keys are unique** — a duplicate key overwrites the earlier value.
- **Keys must be hashable** — only immutable types (str, int, tuple) can be keys, not list, set, or dict.
- **Values can be anything** — any data type, and duplicates are allowed.
- **Ordered by insertion** — keeps the order in which items were added (Python 3.7+).
- **Mutable** — pairs can be added, updated, or removed after creation.
- **Fast lookup** — finding a value by key is very quick.
- **Dynamic size** — grows and shrinks as pairs are added or removed.
- **Can be nested** — a value can be another dictionary.

***Dictionary methods***

| Method | Input | Return | Affects Original Dictionary |
|---|---|---|---|
| `get(key, default)` | Key, optional default (default is `None`) | Value, or default if key is missing (no error) | No |
| `keys()` | Nothing | View of all keys, return type **dict_keys** | No |
| `values()` | Nothing | View of all values, return type **dict_values** | No |
| `items()` | Nothing | View of `(key, value)` tuples, return type **dict_items** | No |
| `update(other)` | Another dict or `key=value` pairs | `None` | Yes |
| `pop(key, default)` | Key, optional default | The removed value (`KeyError` if key is missing and no default) | Yes |
| `popitem()` | Nothing | The last inserted `(key, value)` pair (`KeyError` if empty) | Yes |
| `setdefault(key, default)` | Key, optional default | Value of the key; if the key is missing, adds it with the default | Yes (only if key is missing) |
| `clear()` | Nothing | `None` | Yes |
| `copy()` | Nothing | New dictionary (shallow copy) | No |
| `fromkeys(iterable, value)` | Iterable of keys, optional value | New dictionary | No |

***Operations***

| Operation | Input | Return | Affects Original Dictionary |
|---|---|---|---|
| `d[key]` | Key | Value (`KeyError` if key is missing) | No |
| `d[key] = value` | Key, value | Nothing (adds the pair, or updates the value if key exists) | Yes |
| `del d[key]` | Key | Nothing (`KeyError` if key is missing) | Yes |
| `key in d` | Key | `True` / `False` (checks keys only) | No |
| `d1 \| d2` | Another dictionary | New merged dictionary (Python 3.9+) | No |
| `d1 \|= d2` | Another dictionary | Same dictionary, updated (Python 3.9+) | Yes |
| `{**d1, **d2}` | Two or more dictionaries | New merged dictionary | No |

***Built-in functions on dictionary***

| Function | Input | Return | Affects Original Dictionary |
|---|---|---|---|
| `len(d)` | Dictionary | Number of key-value pairs | No |
| `min(d)` / `max(d)` | Dictionary | Smallest / largest **key** | No |
| `sum(d)` | Dictionary with numeric keys | Total of all **keys** | No |
| `any(d)` / `all(d)` | Dictionary | Result based on the **keys** | No |
| `sorted(d)` | Dictionary, optional `key`, `reverse` | New sorted list of keys | No |
| `list(d)` | Dictionary | List of keys | No |
| `dict(iterable)` | Iterable of pairs, or `zip(keys, values)` | New dictionary | No |

***Key points***

- `d[key]` raises `KeyError` if the key is missing, `get()` returns `None` (or a default) instead.
- Looping over a dictionary gives its keys, use `items()` to get both key and value.
- `keys()`, `values()`, and `items()` return live views, they change when the dictionary changes.
- `update()` adds new keys and overwrites the values of existing keys.

<hr style="border: 2px solid">


<span style="font-size: 2em"><b>&#42;args &amp; &#42;&#42;kwargs</b></span>

- special syntax in Python that allow a function to accept a variable number of arguments.
- The single asterisk (*) and double asterisk (**) are what tell Python to pack the extra inputs. **args** and **kwargs** are just the naming convention
- Used when we don't know how many arguments will be passed to the function.

***`*args`***
 
- args syntax allows a function to accept any number of positional arguments. 
- All passed values are collected into a **tuple**, which can then be accessed or iterated inside the function. 

***`**kwargs`***
 
- kwargs syntax allows a function to accept any number of keyword arguments. 
- All arguments are collected into a **dictionary**, where the argument names become **keys** and their corresponding values become dictionary **values**.

```python
def sum(*args):
    # Function statmenet here args is a tuple , treat it like a tuple
sum(1,2,3)
sum(1,2,3,4,5)

_________________________

def studnet_details(**kwargs):
    # Function statmenet here kwargs is a dictionary , treat it like a dictionary

student_details(name: "XYZ" , adress : "xyz" , Age : val)    

```

<hr style="border: 2px solid">

<span style="font-size: 2em"><b>Decorator</b></span>

A **decorator** is a function that takes another function, adds extra behavior to it, and returns a new function — **without modifying the original function's code**.

**Why it works:** in Python, functions are *first-class objects*. They can be:

- assigned to variables
- passed as arguments
- returned from other functions
- defined inside other functions (closures)

**Common use cases:** logging, timing/performance measurement, authentication/authorization, caching (`functools.lru_cache`), retry logic, input validation, rate limiting.

```python
def my_decorator(func):              # 1. takes a function
    def wrapper(*args, **kwargs):    # 2. defines a wrapper
        # code BEFORE the original function
        result = func(*args, **kwargs)   # 3. calls the original
        # code AFTER the original function
        return result                # 4. returns its result
    return wrapper                   # 5. returns the wrapper (not called!)
```

Key points:

- `return wrapper` — return the function itself, **no parentheses**.
- `*args, **kwargs` — lets the wrapper accept any arguments and forward them to the original function.
- Always `return result` from the wrapper, otherwise the decorated function returns `None`.

***Ways to apply a decorator:***

**1. Manual (explicit assignment)**

```python
new_func = decorator_func(old_function) # new_func is decorated function now
```

**2. Annotation**

```python
@decorator_function
def old_function():
    # old function statements
```

<hr style="border: 2px solid">