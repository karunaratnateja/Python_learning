# Python_learning
This was a Repository that document my python learning and it is used to track my progress to learn python

# Python Day 1 – Introduction and Basics

## 1. What is Python?

Python is a high-level, interpreted, general-purpose programming language. It is easy to learn and uses simple, readable syntax.

## 2. Features and Applications

### Features

* Easy to learn and use
* Interpreted language
* Dynamically typed
* Object-oriented
* Open-source and free
* Cross-platform support
* Large collection of libraries

### Applications

* Web Development
* Artificial Intelligence
* Machine Learning
* Data Science
* Automation
* Game Development
* Cybersecurity

## 3. Python Installation

1. Visit https://www.python.org/downloads/
2. Download Python.
3. Run the installer.
4. Select "Add Python to PATH".
5. Click Install Now.

Verify installation:

```bash
python --version
```

## 4. IDE: VS Code / PyCharm

IDE stands for Integrated Development Environment. It is used to write, run, debug, and manage programs.

**VS Code**

* Lightweight and fast code editor.
* Supports Python through extensions.
* Suitable for multiple programming languages.

**PyCharm**

* Python-focused IDE.
* Provides intelligent code suggestions.
* Supports debugging and project management.

## 5. Interpreter vs Compiler

| Interpreter                                  | Compiler                                            |
| -------------------------------------------- | --------------------------------------------------- |
| Executes code through an interpreter         | Translates source code into another form            |
| Commonly executes instructions progressively | Commonly translates the program before execution    |
| Runtime errors may occur during execution    | Compilation errors can be detected before execution |

Python is generally called an interpreted language.

## 6. First Python Program

```python
print("Hello World")
```

Output:

```text
Hello World
```

The `print()` function is used to display output.

## 7. Comments and Indentation

### Comments

Comments are used to explain code. They are ignored during normal execution.

```python
# This is a single-line comment
print("Hello")
```

### Indentation

Indentation means spaces at the beginning of a line. Python uses indentation to define code blocks.

```python
if 10 > 5:
    print("10 is greater")
```

Python convention is to use 4 spaces for indentation.

## 8. Variables and Naming Rules

A variable is a name that refers to a value.

```python
name = "Python"
age = 20
price = 99.5
```

### Naming Rules

* Must start with a letter or underscore.
* Cannot start with a number.
* Can contain letters, numbers, and underscores.
* Spaces are not allowed.
* Variable names are case-sensitive.
* Python keywords cannot be used as variable names.

Example:

```python
student_name = "Ravi"
age = 21
```

Python supports dynamic typing, so variable types do not need to be declared explicitly.

## 9. print() and input()

### print()

The `print()` function displays output.

```python
print("Hello Python")
print(10 + 20)
```

Output:

```text
Hello Python
30
```

### input()

The `input()` function takes input from the user. It returns a string by default.

```python
name = input("Enter your name: ")
print("Welcome", name)
```

### Example: Sum of Two Numbers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
```

Output:

```text
Sum = 30
```

**Note:** `int()` converts a string into an integer.

---
