<!-- WARNING: This file is auto-generated (cargo dev generate-all). Edit the lint-declarations in 'crates/ty_python_semantic/src/types/diagnostic.rs' if you want to change anything here. -->

# Rules

## `byte-string-type-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20byte-string-type-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L36)
</small>

**What it does**

Checks for byte-strings in type annotation positions.

**Why is this bad?**

Static analysis tools like ty can't analyze type annotations that use byte-string notation.

**Examples**

```python
def test(): -> b"int":
    ...
```

Use instead:
```python
def test(): -> "int":
    ...
```

## `call-non-callable`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20call-non-callable) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L100)
</small>

**What it does**

Checks for calls to non-callable objects.

**Why is this bad?**

Calling a non-callable object will raise a `TypeError` at runtime.

**Examples**

```python
4()  # TypeError: 'int' object is not callable
```

## `conflicting-argument-forms`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20conflicting-argument-forms) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L144)
</small>

**What it does**

Checks whether an argument is used as both a value and a type form in a call.

**Why is this bad?**

Such calls have confusing semantics and often indicate a logic error.

**Examples**

```python
from typing import reveal_type
from ty_extensions import is_singleton

if flag:
    f = repr  # Expects a value
else:
    f = is_singleton  # Expects a type form

f(int)  # error
```

## `conflicting-declarations`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20conflicting-declarations) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L170)
</small>

**What it does**

Checks whether a variable has been declared as two conflicting types.

**Why is this bad**

A variable with two conflicting declarations likely indicates a mistake.
Moreover, it could lead to incorrect or ill-defined type inference for
other code that relies on these variables.

**Examples**

```python
if b:
    a: int
else:
    a: str

a = 1
```

## `conflicting-metaclass`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20conflicting-metaclass) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L195)
</small>

**What it does**

Checks for class definitions where the metaclass of the class
being created would not be a subclass of the metaclasses of
all the class's bases.

**Why is it bad?**

Such a class definition raises a `TypeError` at runtime.

**Examples**

```python
class M1(type): ...
class M2(type): ...
class A(metaclass=M1): ...
class B(metaclass=M2): ...

# TypeError: metaclass conflict
class C(A, B): ...
```

## `cyclic-class-definition`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20cyclic-class-definition) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L221)
</small>

**What it does**

Checks for class definitions in stub files that inherit
(directly or indirectly) from themselves.

**Why is it bad?**

Although forward references are natively supported in stub files,
inheritance cycles are still disallowed, as it is impossible to
resolve a consistent [method resolution order] for a class that
inherits from itself.

**Examples**

```python
# foo.pyi
class A(B): ...
class B(A): ...
```

[method resolution order]: https://docs.python.org/3/glossary.html#term-method-resolution-order

## `duplicate-base`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20duplicate-base) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L286)
</small>

**What it does**

Checks for class definitions with duplicate bases.

**Why is this bad?**

Class definitions with duplicate bases raise `TypeError` at runtime.

**Examples**

```python
class A: ...

# TypeError: duplicate base class
class B(A, A): ...
```

## `duplicate-kw-only`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20duplicate-kw-only) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L307)
</small>

**What it does**

Checks for dataclass definitions with more than one field
annotated with `KW_ONLY`.

**Why is this bad?**

`dataclasses.KW_ONLY` is a special marker used to
emulate the `*` syntax in normal signatures.
It can only be used once per dataclass.

Attempting to annotate two different fields with
it will lead to a runtime error.

**Examples**

```python
from dataclasses import dataclass, KW_ONLY

@dataclass
class A:  # Crash at runtime
    b: int
    _1: KW_ONLY
    c: str
    _2: KW_ONLY
    d: bytes
```

## `escape-character-in-forward-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20escape-character-in-forward-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L120)
</small>

TODO #14889

## `fstring-type-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20fstring-type-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L11)
</small>

**What it does**

Checks for f-strings in type annotation positions.

**Why is this bad?**

Static analysis tools like ty can't analyze type annotations that use f-string notation.

**Examples**

```python
def test(): -> f"int":
    ...
```

Use instead:
```python
def test(): -> "int":
    ...
```

## `implicit-concatenated-string-type-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20implicit-concatenated-string-type-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L86)
</small>

**What it does**

Checks for implicit concatenated strings in type annotation positions.

**Why is this bad?**

Static analysis tools like ty can't analyze type annotations that use implicit concatenated strings.

**Examples**

```python
def test(): -> "Literal[" "5" "]":
    ...
```

Use instead:
```python
def test(): -> "Literal[5]":
    ...
```

## `inconsistent-mro`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20inconsistent-mro) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L449)
</small>

**What it does**

Checks for classes with an inconsistent [method resolution order] (MRO).

**Why is this bad?**

Classes with an inconsistent MRO will raise a `TypeError` at runtime.

**Examples**

```python
class A: ...
class B(A): ...

# TypeError: Cannot create a consistent method resolution order
class C(A, B): ...
```

[method resolution order]: https://docs.python.org/3/glossary.html#term-method-resolution-order

## `index-out-of-bounds`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20index-out-of-bounds) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L473)
</small>

**What it does**

Checks for attempts to use an out of bounds index to get an item from
a container.

**Why is this bad?**

Using an out of bounds index will raise an `IndexError` at runtime.

**Examples**

```python
t = (0, 1, 2)
t[3]  # IndexError: tuple index out of range
```

## `instance-layout-conflict`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20instance-layout-conflict) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L339)
</small>

**What it does**

Checks for classes definitions which will fail at runtime due to
"instance memory layout conflicts".

This error is usually caused by attempting to combine multiple classes
that define non-empty `__slots__` in a class's [Method Resolution Order]
(MRO), or by attempting to combine multiple builtin classes in a class's
MRO.

**Why is this bad?**

Inheriting from bases with conflicting instance memory layouts
will lead to a `TypeError` at runtime.

An instance memory layout conflict occurs when CPython cannot determine
the memory layout instances of a class should have, because the instance
memory layout of one of its bases conflicts with the instance memory layout
of one or more of its other bases.

For example, if a Python class defines non-empty `__slots__`, this will
impact the memory layout of instances of that class. Multiple inheritance
from more than one different class defining non-empty `__slots__` is not
allowed:

```python
class A:
    __slots__ = ("a", "b")

class B:
    __slots__ = ("a", "b")  # Even if the values are the same

# TypeError: multiple bases have instance lay-out conflict
class C(A, B): ...
```

An instance layout conflict can also be caused by attempting to use
multiple inheritance with two builtin classes, due to the way that these
classes are implemented in a CPython C extension:

```python
class A(int, float): ...  # TypeError: multiple bases have instance lay-out conflict
```

Note that pure-Python classes with no `__slots__`, or pure-Python classes
with empty `__slots__`, are always compatible:

```python
class A: ...
class B:
    __slots__ = ()
class C:
    __slots__ = ("a", "b")

# fine
class D(A, B, C): ...
```

**Known problems**

Classes that have "dynamic" definitions of `__slots__` (definitions do not consist
of string literals, or tuples of string literals) are not currently considered solid
bases by ty.

Additionally, this check is not exhaustive: many C extensions (including several in
the standard library) define classes that use extended memory layouts and thus cannot
coexist in a single MRO. Since it is currently not possible to represent this fact in
stub files, having a full knowledge of these classes is also impossible. When it comes
to classes that do not define `__slots__` at the Python level, therefore, ty, currently
only hard-codes a number of cases where it knows that a class will produce instances with
an atypical memory layout.

**Further reading**

- [CPython documentation: `__slots__`](https://docs.python.org/3/reference/datamodel.html#slots)
- [CPython documentation: Method Resolution Order](https://docs.python.org/3/glossary.html#term-method-resolution-order)

[Method Resolution Order]: https://docs.python.org/3/glossary.html#term-method-resolution-order

## `invalid-argument-type`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-argument-type) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L493)
</small>

**What it does**

Detects call arguments whose type is not assignable to the corresponding typed parameter.

**Why is this bad?**

Passing an argument of a type the function (or callable object) does not accept violates
the expectations of the function author and may cause unexpected runtime errors within the
body of the function.

**Examples**

```python
def func(x: int): ...
func("foo")  # error: [invalid-argument-type]
```

## `invalid-assignment`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-assignment) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L533)
</small>

**What it does**

Checks for assignments where the type of the value
is not [assignable to] the type of the assignee.

**Why is this bad?**

Such assignments break the rules of the type system and
weaken a type checker's ability to accurately reason about your code.

**Examples**

```python
a: int = ''
```

[assignable to]: https://typing.python.org/en/latest/spec/glossary.html#term-assignable

## `invalid-attribute-access`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-attribute-access) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1537)
</small>

**What it does**

Checks for assignments to class variables from instances
and assignments to instance variables from its class.

**Why is this bad?**

Incorrect assignments break the rules of the type system and
weaken a type checker's ability to accurately reason about your code.

**Examples**

```python
class C:
    class_var: ClassVar[int] = 1
    instance_var: int

C.class_var = 3  # okay
C().class_var = 3  # error: Cannot assign to class variable

C().instance_var = 3  # okay
C.instance_var = 3  # error: Cannot assign to instance variable
```

## `invalid-base`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-base) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L555)
</small>

**What it does**

Checks for class definitions that have bases which are not instances of `type`.

**Why is this bad?**

Class definitions with bases like this will lead to `TypeError` being raised at runtime.

**Examples**

```python
class A(42): ...  # error: [invalid-base]
```

## `invalid-context-manager`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-context-manager) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L606)
</small>

**What it does**

Checks for expressions used in `with` statements
that do not implement the context manager protocol.

**Why is this bad?**

Such a statement will raise `TypeError` at runtime.

**Examples**

```python
# TypeError: 'int' object does not support the context manager protocol
with 1:
    print(2)
```

## `invalid-declaration`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-declaration) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L627)
</small>

**What it does**

Checks for declarations where the inferred type of an existing symbol
is not [assignable to] its post-hoc declared type.

**Why is this bad?**

Such declarations break the rules of the type system and
weaken a type checker's ability to accurately reason about your code.

**Examples**

```python
a = 1
a: str
```

[assignable to]: https://typing.python.org/en/latest/spec/glossary.html#term-assignable

## `invalid-exception-caught`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-exception-caught) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L650)
</small>

**What it does**

Checks for exception handlers that catch non-exception classes.

**Why is this bad?**

Catching classes that do not inherit from `BaseException` will raise a TypeError at runtime.

**Example**

```python
try:
    1 / 0
except 1:
    ...
```

Use instead:
```python
try:
    1 / 0
except ZeroDivisionError:
    ...
```

**References**

- [Python documentation: except clause](https://docs.python.org/3/reference/compound_stmts.html#except-clause)
- [Python documentation: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

**Ruff rule**

 This rule corresponds to Ruff's [`except-with-non-exception-classes` (`B030`)](https://docs.astral.sh/ruff/rules/except-with-non-exception-classes)

## `invalid-generic-class`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-generic-class) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L686)
</small>

**What it does**

Checks for the creation of invalid generic classes

**Why is this bad?**

There are several requirements that you must follow when defining a generic class.

**Examples**

```python
from typing import Generic, TypeVar

T = TypeVar("T")  # okay

# error: class uses both PEP-695 syntax and legacy syntax
class C[U](Generic[T]): ...
```

**References**

- [Typing spec: Generics](https://typing.python.org/en/latest/spec/generics.html#introduction)

## `invalid-legacy-type-variable`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-legacy-type-variable) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L712)
</small>

**What it does**

Checks for the creation of invalid legacy `TypeVar`s

**Why is this bad?**

There are several requirements that you must follow when creating a legacy `TypeVar`.

**Examples**

```python
from typing import TypeVar

T = TypeVar("T")  # okay
Q = TypeVar("S")  # error: TypeVar name must match the variable it's assigned to
T = TypeVar("T")  # error: TypeVars should not be redefined

# error: TypeVar must be immediately assigned to a variable
def f(t: TypeVar("U")): ...
```

**References**

- [Typing spec: Generics](https://typing.python.org/en/latest/spec/generics.html#introduction)

## `invalid-metaclass`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-metaclass) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L761)
</small>

**What it does**

Checks for arguments to `metaclass=` that are invalid.

**Why is this bad?**

Python allows arbitrary expressions to be used as the argument to `metaclass=`.
These expressions, however, need to be callable and accept the same arguments
as `type.__new__`.

**Example**


```python
def f(): ...

# TypeError: f() takes 0 positional arguments but 3 were given
class B(metaclass=f): ...
```

**References**

- [Python documentation: Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)

## `invalid-overload`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-overload) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L788)
</small>

**What it does**

Checks for various invalid `@overload` usages.

**Why is this bad?**

The `@overload` decorator is used to define functions and methods that accepts different
combinations of arguments and return different types based on the arguments passed. This is
mainly beneficial for type checkers. But, if the `@overload` usage is invalid, the type
checker may not be able to provide correct type information.

**Example**


Defining only one overload:

```py
from typing import overload

@overload
def foo(x: int) -> int: ...
def foo(x: int | None) -> int | None:
    return x
```

Or, not providing an implementation for the overloaded definition:

```py
from typing import overload

@overload
def foo() -> None: ...
@overload
def foo(x: int) -> int: ...
```

**References**

- [Python documentation: `@overload`](https://docs.python.org/3/library/typing.html#typing.overload)

## `invalid-parameter-default`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-parameter-default) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L831)
</small>

**What it does**

Checks for default values that can't be
assigned to the parameter's annotated type.

**Why is this bad?**

This breaks the rules of the type system and
weakens a type checker's ability to accurately reason about your code.

**Examples**

```python
def f(a: int = ''): ...
```

## `invalid-protocol`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-protocol) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L421)
</small>

**What it does**

Checks for invalidly defined protocol classes.

**Why is this bad?**

An invalidly defined protocol class may lead to the type checker inferring
unexpected things. It may also lead to `TypeError`s at runtime.

**Examples**

A `Protocol` class cannot inherit from a non-`Protocol` class;
this raises a `TypeError` at runtime:

```pycon
>>> from typing import Protocol
>>> class Foo(int, Protocol): ...
...
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    class Foo(int, Protocol): ...
TypeError: Protocols can only inherit from other protocols, got <class 'int'>
```

## `invalid-raise`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-raise) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L851)
</small>

Checks for `raise` statements that raise non-exceptions or use invalid
causes for their raised exceptions.

**Why is this bad?**

Only subclasses or instances of `BaseException` can be raised.
For an exception's cause, the same rules apply, except that `None` is also
permitted. Violating these rules results in a `TypeError` at runtime.

**Examples**

```python
def f():
    try:
        something()
    except NameError:
        raise "oops!" from f

def g():
    raise NotImplemented from 42
```

Use instead:
```python
def f():
    try:
        something()
    except NameError as e:
        raise RuntimeError("oops!") from e

def g():
    raise NotImplementedError from None
```

**References**

- [Python documentation: The `raise` statement](https://docs.python.org/3/reference/simple_stmts.html#raise)
- [Python documentation: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

## `invalid-return-type`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-return-type) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L514)
</small>

**What it does**

Detects returned values that can't be assigned to the function's annotated return type.

**Why is this bad?**

Returning an object of a type incompatible with the annotated return type may cause confusion to the user calling the function.

**Examples**

```python
def func() -> int:
    return "a"  # error: [invalid-return-type]
```

## `invalid-super-argument`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-super-argument) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L894)
</small>

**What it does**

Detects `super()` calls where:
- the first argument is not a valid class literal, or
- the second argument is not an instance or subclass of the first argument.

**Why is this bad?**

`super(type, obj)` expects:
- the first argument to be a class,
- and the second argument to satisfy one of the following:
  - `isinstance(obj, type)` is `True`
  - `issubclass(obj, type)` is `True`

Violating this relationship will raise a `TypeError` at runtime.

**Examples**

```python
class A:
    ...
class B(A):
    ...

super(A, B())  # it's okay! `A` satisfies `isinstance(B(), A)`

super(A(), B()) # error: `A()` is not a class

super(B, A())  # error: `A()` does not satisfy `isinstance(A(), B)`
super(B, A)  # error: `A` does not satisfy `issubclass(A, B)`
```

**References**

- [Python documentation: super()](https://docs.python.org/3/library/functions.html#super)

## `invalid-syntax-in-forward-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-syntax-in-forward-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L111)
</small>

TODO #14889

## `invalid-type-alias-type`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-alias-type) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L740)
</small>

**What it does**

Checks for the creation of invalid `TypeAliasType`s

**Why is this bad?**

There are several requirements that you must follow when creating a `TypeAliasType`.

**Examples**

```python
from typing import TypeAliasType

IntOrStr = TypeAliasType("IntOrStr", int | str)  # okay
NewAlias = TypeAliasType(get_name(), int)        # error: TypeAliasType name must be a string literal
```

## `invalid-type-checking-constant`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-checking-constant) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L933)
</small>

**What it does**

Checks for a value other than `False` assigned to the `TYPE_CHECKING` variable, or an
annotation not assignable from `bool`.

**Why is this bad?**

The name `TYPE_CHECKING` is reserved for a flag that can be used to provide conditional
code seen only by the type checker, and not at runtime. Normally this flag is imported from
`typing` or `typing_extensions`, but it can also be defined locally. If defined locally, it
must be assigned the value `False` at runtime; the type checker will consider its value to
be `True`. If annotated, it must be annotated as a type that can accept `bool` values.

**Examples**

```python
TYPE_CHECKING: str
TYPE_CHECKING = ''
```

## `invalid-type-form`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-form) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L957)
</small>

**What it does**

Checks for expressions that are used as [type expressions]
but cannot validly be interpreted as such.

**Why is this bad?**

Such expressions cannot be understood by ty.
In some cases, they might raise errors at runtime.

**Examples**

```python
from typing import Annotated

a: type[1]  # `1` is not a type
b: Annotated[int]  # `Annotated` expects at least two arguments
```
[type expressions]: https://typing.python.org/en/latest/spec/annotations.html#type-and-annotation-expressions

## `invalid-type-guard-call`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-guard-call) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1009)
</small>

**What it does**

Checks for type guard function calls without a valid target.

**Why is this bad?**

The first non-keyword non-variadic argument to a type guard function
is its target and must map to a symbol.

Starred (`is_str(*a)`), literal (`is_str(42)`) and other non-symbol-like
expressions are invalid as narrowing targets.

**Examples**

```python
from typing import TypeIs

def f(v: object) -> TypeIs[int]: ...

f()  # Error
f(*a)  # Error
f(10)  # Error
```

## `invalid-type-guard-definition`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-guard-definition) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L981)
</small>

**What it does**

Checks for type guard functions without
a first non-self-like non-keyword-only non-variadic parameter.

**Why is this bad?**

Type narrowing functions must accept at least one positional argument
(non-static methods must accept another in addition to `self`/`cls`).

Extra parameters/arguments are allowed but do not affect narrowing.

**Examples**

```python
from typing import TypeIs

def f() -> TypeIs[int]: ...  # Error, no parameter
def f(*, v: object) -> TypeIs[int]: ...  # Error, no positional arguments allowed
def f(*args: object) -> TypeIs[int]: ... # Error, expect variadic arguments
class C:
    def f(self) -> TypeIs[int]: ...  # Error, only positional argument expected is `self`
```

## `invalid-type-variable-constraints`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-type-variable-constraints) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1037)
</small>

**What it does**

Checks for constrained [type variables] with only one constraint.

**Why is this bad?**

A constrained type variable must have at least two constraints.

**Examples**

```python
from typing import TypeVar

T = TypeVar('T', str)  # invalid constrained TypeVar
```

Use instead:
```python
T = TypeVar('T', str, int)  # valid constrained TypeVar
# or
T = TypeVar('T', bound=str)  # valid bound TypeVar
```

[type variables]: https://docs.python.org/3/library/typing.html#typing.TypeVar

## `missing-argument`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20missing-argument) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1066)
</small>

**What it does**

Checks for missing required arguments in a call.

**Why is this bad?**

Failing to provide a required argument will raise a `TypeError` at runtime.

**Examples**

```python
def func(x: int): ...
func()  # TypeError: func() missing 1 required positional argument: 'x'
```

## `no-matching-overload`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20no-matching-overload) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1085)
</small>

**What it does**

Checks for calls to an overloaded function that do not match any of the overloads.

**Why is this bad?**

Failing to provide the correct arguments to one of the overloads will raise a `TypeError`
at runtime.

**Examples**

```python
@overload
def func(x: int): ...
@overload
def func(x: bool): ...
func("string")  # error: [no-matching-overload]
```

## `non-subscriptable`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20non-subscriptable) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1108)
</small>

**What it does**

Checks for subscripting objects that do not support subscripting.

**Why is this bad?**

Subscripting an object that does not support it will raise a `TypeError` at runtime.

**Examples**

```python
4[1]  # TypeError: 'int' object is not subscriptable
```

## `not-iterable`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20not-iterable) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1126)
</small>

**What it does**

Checks for objects that are not iterable but are used in a context that requires them to be.

**Why is this bad?**

Iterating over an object that is not iterable will raise a `TypeError` at runtime.

**Examples**


```python
for i in 34:  # TypeError: 'int' object is not iterable
    pass
```

## `parameter-already-assigned`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20parameter-already-assigned) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1177)
</small>

**What it does**

Checks for calls which provide more than one argument for a single parameter.

**Why is this bad?**

Providing multiple values for a single parameter will raise a `TypeError` at runtime.

**Examples**


```python
def f(x: int) -> int: ...

f(1, x=2)  # Error raised here
```

## `raw-string-type-annotation`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20raw-string-type-annotation) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fstring_annotation.rs#L61)
</small>

**What it does**

Checks for raw-strings in type annotation positions.

**Why is this bad?**

Static analysis tools like ty can't analyze type annotations that use raw-string notation.

**Examples**

```python
def test(): -> r"int":
    ...
```

Use instead:
```python
def test(): -> "int":
    ...
```

## `static-assert-error`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20static-assert-error) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1513)
</small>

**What it does**

Makes sure that the argument of `static_assert` is statically known to be true.

**Why is this bad?**

A `static_assert` call represents an explicit request from the user
for the type checker to emit an error if the argument cannot be verified
to evaluate to `True` in a boolean context.

**Examples**

```python
from ty_extensions import static_assert

static_assert(1 + 1 == 3)  # error: evaluates to `False`

static_assert(int(2.0 * 3.0) == 6)  # error: does not have a statically known truthiness
```

## `subclass-of-final-class`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20subclass-of-final-class) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1268)
</small>

**What it does**

Checks for classes that subclass final classes.

**Why is this bad?**

Decorating a class with `@final` declares to the type checker that it should not be subclassed.

**Example**


```python
from typing import final

@final
class A: ...
class B(A): ...  # Error raised here
```

## `too-many-positional-arguments`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20too-many-positional-arguments) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1313)
</small>

**What it does**

Checks for calls that pass more positional arguments than the callable can accept.

**Why is this bad?**

Passing too many positional arguments will raise `TypeError` at runtime.

**Example**


```python
def f(): ...

f("foo")  # Error raised here
```

## `type-assertion-failure`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20type-assertion-failure) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1291)
</small>

**What it does**

Checks for `assert_type()` and `assert_never()` calls where the actual type
is not the same as the asserted type.

**Why is this bad?**

`assert_type()` allows confirming the inferred type of a certain value.

**Example**


```python
def _(x: int):
    assert_type(x, int)  # fine
    assert_type(x, str)  # error: Actual type does not match asserted type
```

## `unavailable-implicit-super-arguments`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unavailable-implicit-super-arguments) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1334)
</small>

**What it does**

Detects invalid `super()` calls where implicit arguments like the enclosing class or first method argument are unavailable.

**Why is this bad?**

When `super()` is used without arguments, Python tries to find two things:
the nearest enclosing class and the first argument of the immediately enclosing function (typically self or cls).
If either of these is missing, the call will fail at runtime with a `RuntimeError`.

**Examples**

```python
super()  # error: no enclosing class or function found

def func():
    super()  # error: no enclosing class or first argument exists

class A:
    f = super()  # error: no enclosing function to provide the first argument

    def method(self):
        def nested():
            super()  # error: first argument does not exist in this nested function

        lambda: super()  # error: first argument does not exist in this lambda

        (super() for _ in range(10))  # error: argument is not available in generator expression

        super()  # okay! both enclosing class and first argument are available
```

**References**

- [Python documentation: super()](https://docs.python.org/3/library/functions.html#super)

## `unknown-argument`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unknown-argument) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1391)
</small>

**What it does**

Checks for keyword arguments in calls that don't match any parameter of the callable.

**Why is this bad?**

Providing an unknown keyword argument will raise `TypeError` at runtime.

**Example**


```python
def f(x: int) -> int: ...

f(x=1, y=2)  # Error raised here
```

## `unresolved-attribute`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unresolved-attribute) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1412)
</small>

**What it does**

Checks for unresolved attributes.

**Why is this bad?**

Accessing an unbound attribute will raise an `AttributeError` at runtime.
An unresolved attribute is not guaranteed to exist from the type alone,
so this could also indicate that the object is not of the type that the user expects.

**Examples**

```python
class A: ...

A().foo  # AttributeError: 'A' object has no attribute 'foo'
```

## `unresolved-import`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unresolved-import) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1434)
</small>

**What it does**

Checks for import statements for which the module cannot be resolved.

**Why is this bad?**

Importing a module that cannot be resolved will raise a `ModuleNotFoundError`
at runtime.

**Examples**

```python
import foo  # ModuleNotFoundError: No module named 'foo'
```

## `unresolved-reference`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unresolved-reference) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1453)
</small>

**What it does**

Checks for references to names that are not defined.

**Why is this bad?**

Using an undefined variable will raise a `NameError` at runtime.

**Example**


```python
print(x)  # NameError: name 'x' is not defined
```

## `unsupported-bool-conversion`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unsupported-bool-conversion) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1146)
</small>

**What it does**

Checks for bool conversions where the object doesn't correctly implement `__bool__`.

**Why is this bad?**

If an exception is raised when you attempt to evaluate the truthiness of an object,
using the object in a boolean context will fail at runtime.

**Examples**


```python
class NotBoolable:
    __bool__ = None

b1 = NotBoolable()
b2 = NotBoolable()

if b1:  # exception raised here
    pass

b1 and b2  # exception raised here
not b1  # exception raised here
b1 < b2 < b1  # exception raised here
```

## `unsupported-operator`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unsupported-operator) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1472)
</small>

**What it does**

Checks for binary expressions, comparisons, and unary expressions where
the operands don't support the operator.

**Why is this bad?**

Attempting to use an unsupported operator will raise a `TypeError` at
runtime.

**Examples**

```python
class A: ...

A() + A()  # TypeError: unsupported operand type(s) for +: 'A' and 'A'
```

## `zero-stepsize-in-slice`

<small>
Default level: [`error`](../rules.md#rule-levels "This lint has a default level of 'error'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20zero-stepsize-in-slice) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1494)
</small>

**What it does**

Checks for step size 0 in slices.

**Why is this bad?**

A slice with a step size of zero will raise a `ValueError` at runtime.

**Examples**

```python
l = list(range(10))
l[1:10:0]  # ValueError: slice step cannot be zero
```

## `deprecated`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20deprecated) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L265)
</small>

**What it does**

Checks for uses of deprecated items

**Why is this bad?**

Deprecated items should no longer be used.

**Examples**

```python
@warnings.deprecated("use new_func instead")
def old_func(): ...

old_func()  # emits [deprecated] diagnostic
```

## `invalid-ignore-comment`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20invalid-ignore-comment) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Fsuppression.rs#L65)
</small>

**What it does**

Checks for `type: ignore` and `ty: ignore` comments that are syntactically incorrect.

**Why is this bad?**

A syntactically incorrect ignore comment is probably a mistake and is useless.

**Examples**

```py
a = 20 / 0  # type: ignoree
```

Use instead:

```py
a = 20 / 0  # type: ignore
```

## `possibly-unbound-attribute`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20possibly-unbound-attribute) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1198)
</small>

**What it does**

Checks for possibly unbound attributes.

**Why is this bad?**

Attempting to access an unbound attribute will raise an `AttributeError` at runtime.

**Examples**

```python
class A:
    if b:
        c = 0

A.c  # AttributeError: type object 'A' has no attribute 'c'
```

## `possibly-unbound-implicit-call`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20possibly-unbound-implicit-call) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L118)
</small>

**What it does**

Checks for implicit calls to possibly unbound methods.

**Why is this bad?**

Expressions such as `x[y]` and `x * y` call methods
under the hood (`__getitem__` and `__mul__` respectively).
Calling an unbound method will raise an `AttributeError` at runtime.

**Examples**

```python
import datetime

class A:
    if datetime.date.today().weekday() != 6:
        def __getitem__(self, v): ...

A()[0]  # TypeError: 'A' object is not subscriptable
```

## `possibly-unbound-import`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20possibly-unbound-import) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1220)
</small>

**What it does**

Checks for imports of symbols that may be unbound.

**Why is this bad?**

Importing an unbound module or name will raise a `ModuleNotFoundError`
or `ImportError` at runtime.

**Examples**

```python
# module.py
import datetime

if datetime.date.today().weekday() != 6:
    a = 1

# main.py
from module import a  # ImportError: cannot import name 'a' from 'module'
```

## `redundant-cast`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20redundant-cast) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1565)
</small>

**What it does**

Detects redundant `cast` calls where the value already has the target type.

**Why is this bad?**

These casts have no effect and can be removed.

**Example**

```python
def f() -> int:
    return 10

cast(int, f())  # Redundant
```

## `undefined-reveal`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20undefined-reveal) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1373)
</small>

**What it does**

Checks for calls to `reveal_type` without importing it.

**Why is this bad?**

Using `reveal_type` without importing it will raise a `NameError` at runtime.

**Examples**

```python
reveal_type(1)  # NameError: name 'reveal_type' is not defined
```

## `unknown-rule`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unknown-rule) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Fsuppression.rs#L40)
</small>

**What it does**

Checks for `ty: ignore[code]` where `code` isn't a known lint rule.

**Why is this bad?**

A `ty: ignore[code]` directive with a `code` that doesn't match
any known rule will not suppress any type errors, and is probably a mistake.

**Examples**

```py
a = 20 / 0  # ty: ignore[division-by-zer]
```

Use instead:

```py
a = 20 / 0  # ty: ignore[division-by-zero]
```

## `unresolved-global`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unresolved-global) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1586)
</small>

**What it does**

Detects variables declared as `global` in an inner scope that have no explicit
bindings or declarations in the global scope.

**Why is this bad?**

Function bodies with `global` statements can run in any order (or not at all), which makes
it hard for static analysis tools to infer the types of globals without
explicit definitions or declarations.

**Example**

```python
def f():
    global x  # unresolved global
    x = 42

def g():
    print(x)  # unresolved reference
```

Use instead:
```python
x: int

def f():
    global x
    x = 42

def g():
    print(x)
```

Or:
```python
x: int | None = None

def f():
    global x
    x = 42

def g():
    print(x)
```

## `unsupported-base`

<small>
Default level: [`warn`](../rules.md#rule-levels "This lint has a default level of 'warn'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unsupported-base) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L573)
</small>

**What it does**

Checks for class definitions that have bases which are unsupported by ty.

**Why is this bad?**

If a class has a base that is an instance of a complex type such as a union type,
ty will not be able to resolve the [method resolution order] (MRO) for the class.
This will lead to an inferior understanding of your codebase and unpredictable
type-checking behavior.

**Examples**

```python
import datetime

class A: ...
class B: ...

if datetime.date.today().weekday() != 6:
    C = A
else:
    C = B

class D(C): ...  # error: [unsupported-base]
```

[method resolution order]: https://docs.python.org/3/glossary.html#term-method-resolution-order

## `division-by-zero`

<small>
Default level: [`ignore`](../rules.md#rule-levels "This lint has a default level of 'ignore'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20division-by-zero) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L247)
</small>

**What it does**

It detects division by zero.

**Why is this bad?**

Dividing by zero raises a `ZeroDivisionError` at runtime.

**Examples**

```python
5 / 0
```

## `possibly-unresolved-reference`

<small>
Default level: [`ignore`](../rules.md#rule-levels "This lint has a default level of 'ignore'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20possibly-unresolved-reference) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Ftypes%2Fdiagnostic.rs#L1246)
</small>

**What it does**

Checks for references to names that are possibly not defined.

**Why is this bad?**

Using an undefined variable will raise a `NameError` at runtime.

**Example**


```python
for i in range(0):
    x = i

print(x)  # NameError: name 'x' is not defined
```

## `unused-ignore-comment`

<small>
Default level: [`ignore`](../rules.md#rule-levels "This lint has a default level of 'ignore'.") ·
[Related issues](https://github.com/astral-sh/ty/issues?q=sort%3Aupdated-desc%20is%3Aissue%20is%3Aopen%20unused-ignore-comment) ·
[View source](https://github.com/astral-sh/ruff/blob/main/crates%2Fty_python_semantic%2Fsrc%2Fsuppression.rs#L15)
</small>

**What it does**

Checks for `type: ignore` or `ty: ignore` directives that are no longer applicable.

**Why is this bad?**

A `type: ignore` directive that no longer matches any diagnostic violations is likely
included by mistake, and should be removed to avoid confusion.

**Examples**

```py
a = 20 / 2  # ty: ignore[division-by-zero]
```

Use instead:

```py
a = 20 / 2
```

