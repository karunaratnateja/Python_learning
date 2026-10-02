# Python Day 2 – Data Types

## 1. What are Data Types?

Data types define the type of value stored in a variable.

Python has several built-in data types, such as integers, floats, strings, booleans, and more.

## 2. Integer (int)

The `int` data type is used to store whole numbers without decimal points.

```python
age = 21
marks = 95
negative = -10

print(age)
print(type(age))
```

Output:

```text
21
<class 'int'>
```

## 3. Float (float)

The `float` data type is used to store numbers with decimal points.

```python
price = 99.5
percentage = 85.75

print(price)
print(type(price))
```

Output:

```text
99.5
<class 'float'>
```

## 4. Complex (complex)

The `complex` data type represents numbers with real and imaginary parts.

```python
x = 3 + 4j

print(x)
print(type(x))
print(x.real)
print(x.imag)
```

Output:

```text
(3+4j)
<class 'complex'>
3.0
4.0
```

Note: Python uses `j` to represent the imaginary part.

## 5. String (str)

The `str` data type is used to store text or a sequence of characters.

Strings can be written using single, double, or triple quotes.

```python
name = "Python"
language = 'Programming'
message = """Welcome to Python"""

print(name)
print(type(name))
```

Output:

```text
Python
<class 'str'>
```

## 6. Boolean (bool)

The `bool` data type represents two values: `True` and `False`.

It is commonly used in conditions and decision-making.

```python
a = True
b = False

print(a)
print(type(a))
```

Output:

```text
True
<class 'bool'>
```

Note: `True` and `False` must start with capital letters.

## 7. NoneType

`None` represents the absence of a value.

It is commonly used to indicate that a variable has no assigned meaningful value.

```python
x = None

print(x)
print(type(x))
```

Output:

```text
None
<class 'NoneType'>
```

## 8. Type Checking Using type()

The `type()` function is used to identify the data type of a value or variable.

```python
a = 10
b = 10.5
c = "Hello"
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>
```

## 9. Type Conversion / Type Casting

Type casting means converting a value from one data type to another.

### Common Type Conversion Functions

| Function    | Conversion          |
| ----------- | ------------------- |
| `int()`     | Converts to integer |
| `float()`   | Converts to float   |
| `str()`     | Converts to string  |
| `bool()`    | Converts to boolean |
| `complex()` | Converts to complex |

### Example

```python
a = "100"
b = int(a)

print(b)
print(type(b))
```

Output:

```text
100
<class 'int'>
```

### More Examples

```python
x = 10
print(float(x))

y = 25.5
print(int(y))

z = 100
print(str(z))
```

Output:

```text
10.0
25
100
```

Note: `int(25.5)` removes the decimal part; it does not round the number.

### Implicit Type Conversion

Python automatically converts certain values to a compatible type during operations.

```python
a = 10
b = 2.5

c = a + b

print(c)
print(type(c))
```

Output:

```text
12.5
<class 'float'>
```

## 10. Mutable vs Immutable

### Mutable

Mutable objects can be changed after creation without creating a new object.

Examples:

* list
* dict
* set

```python
numbers = [10, 20, 30]
numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

### Immutable

Immutable objects cannot be changed after creation.

Examples:

* int
* float
* complex
* str
* bool
* tuple
* frozenset
* NoneType

```python
name = "Python"
name = "Java"

print(name)
```

Output:

```text
Java
```

Here, the original string is not modified. The variable is reassigned to a new string object.

### Difference

| Mutable                        | Immutable                          |
| ------------------------------ | ---------------------------------- |
| Can be modified after creation | Cannot be modified after creation  |
| Example: list                  | Example: tuple                     |
| Supports item modification     | Does not support item modification |

## 11. id() and Object Identity

The `id()` function returns the identity of an object.

It is commonly used to observe whether two variables refer to the same object.

```python
a = 10
b = a

print(id(a))
print(id(b))
print(a is b)
```

Output:

```text
Same identity value
Same identity value
True
```

Note: The actual identity values depend on the Python execution.

### Example with Mutable Objects

```python
a = [10, 20]
b = a

print(a is b)

b.append(30)

print(a)
print(b)
```

Output:

```text
True
[10, 20, 30]
[10, 20, 30]
```

Both variables refer to the same list object. Therefore, changes through one variable are visible through the other.

### `is` vs `==`

* `==` checks whether two values are equal.
* `is` checks whether two variables refer to the same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

---

## Day 2 Summary

| Concept      | Description                  |
| ------------ | ---------------------------- |
| int          | Whole numbers                |
| float        | Decimal numbers              |
| complex      | Real and imaginary numbers   |
| str          | Text data                    |
| bool         | True or False                |
| NoneType     | Absence of a value           |
| type()       | Checks data type             |
| Type Casting | Converts one type to another |
| Mutable      | Object can be modified       |
| Immutable    | Object cannot be modified    |
| id()         | Returns object identity      |
| is           | Checks object identity       |
| ==           | Checks value equality        |

