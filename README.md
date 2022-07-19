# 💩 PyOOPy 💩
**P**ython **O**bject-**O**riented **P**rogramming library

## Installation
```pip install PyOOPy```

## Usage
### Example  usage
```python
from PyOOPy import PyOOPy, Private

class Class(metaclass=PyOOPy):
    private_class_field: Private[str] = 'private_class_field'
    
    def __init__(self, private_obj_field: Private):
        self.private_obj_field = private_obj_field

    def private_method(self) -> Private[str]:
        return 'private_method'

class PrivateClass(metaclass=PyOOPy):
    # Makes all the fields and methods private by default
    def __init__(self) -> Private:
        pass
```
### Protected, Private & Public
```python
from PyOOPy import PyOOPy, Protected, Private, Public

class Class(metaclass=PyOOPy):
    protected_field: Protected[str] = 'protected_field'
    private_field: Private[str] = 'private_field'
    public_field: Public[str] = 'public_field'

    def protected_method(self) -> Protected[str]:
        return 'protected_method'

    def private_method(self) -> Private[str]:
        return 'private_method'

    def public_method(self) -> Public[str]:
        return 'public_method'
```
### Final
```python
from PyOOPy import PyOOPy, Final

class Class(metaclass=PyOOPy):
    final_field: Final[str] = 'final_field'

    def final_method(self) -> Final[str]:
        return 'final_method'
```
### Abstract
```python
from PyOOPy import PyOOPy, Abstract

class Class(metaclass=PyOOPy):
    def __init__(self) -> Abstract:
        pass
```