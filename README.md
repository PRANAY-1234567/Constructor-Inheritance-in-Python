# 🧬 Constructor Inheritance in Python

## 📌 Description

This Python program demonstrates **constructor inheritance**.
When an object of the child class `Derived` is created, the constructor of the parent class `Base` is automatically called because the child class does not define its own constructor.

---

## 🚀 Features

* Demonstrates **inheritance**
* Shows automatic constructor calling
* Explains parent-child constructor relationship

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Base`

Contains a constructor:

```python id="z2m8pl"
def __init__(self):
```

This constructor prints:

```python id="u7x3qa"
Inside class Base default constructor
```

---

### 2️⃣ Child Class – `Derived`

```python id="n4k9mv"
class Derived(Base):
    pass
```

👉 `Derived` inherits from `Base`

👉 `pass` means:

* no additional code
* no constructor
* no methods

---

### 3️⃣ Object Creation

```python id="f8m2zx"
obj = Derived()
```

Since `Derived` has no constructor, Python automatically calls:

```python id="r3q7pt"
Base.__init__()
```

---

## 💻 Code

```python id="w1x8pl"
class Base:
    def __init__(self):
        print("Inside class Base default constructor")

class Derived(Base):
    pass

class Inh8:
    @staticmethod
    def main():
        obj = Derived()

Inh8.main()
```

---

## ▶️ Output

```id="m7k2qa"
Inside class Base default constructor
```

---

## 🧠 Key Concept

### ✔ Constructor Inheritance

If child class does not define:

```python id="c9x4mv"
__init__()
```

then parent constructor is automatically used.

---

## 📚 Concepts Used

* Class & Object
* Inheritance
* Constructor (`__init__`)
* Parent-child relationship

---

## 🔥 Important Understanding

### Child class without constructor

```python id="d4m8zx"
class Derived(Base):
    pass
```

👉 Uses parent constructor automatically.

---

### Child class with constructor

If child class has its own constructor:

```python id="y6q3pt"
class Derived(Base):
    def __init__(self):
        print("Derived constructor")
```

👉 Parent constructor will NOT run automatically.

You must explicitly call:

```python id="s2x7mv"
super().__init__()
```

---

## ⚡ Example with `super()`

```python id="p9m1qa"
class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived constructor")
```

### Output

```text id="j5k8zx"
Inside class Base default constructor
Inside Derived constructor
```

---

## 🎯 Use Case

This concept is important for:

* Code reuse
* Initializing inherited properties
* Large OOP projects

---

## 🔧 Future Improvements

* Add derived constructor
* Demonstrate multilevel inheritance
* Show constructor overriding
* Add parameterized constructors

---

## 📄 License

This project is open-source and free to use.


<img width="620" height="582" alt="image" src="https://github.com/user-attachments/assets/f4fbeb84-86e5-458b-a71f-c7af8e6650a0" />
