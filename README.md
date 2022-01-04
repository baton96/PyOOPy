# 💩 PyOOPy 💩
**P**ython **O**bject-**O**riented **P**rogramming library

## Installation
```pip install PyOOPy```

## Usage
### Example  usage
```python
from PyOOPy import PyOOPy, Private

class Class(metaclass=PyOOPy):
    private_class_field: Private = 'private_class_field'
    
    def __init__(self, private_obj_field: Private):
        self.private_obj_field = private_obj_field

    def private_method(self) -> Private:
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
    protected_field: Protected = 'protected_field'
    private_field: Private = 'private_field'
    public_field: Public = 'public_field'

    def protected_method(self) -> Protected:
        return 'protected_method'

    def private_method(self) -> Private:
        return 'private_method'

    def public_method(self) -> Public:
        return 'public_method'
```
### Final
```python
from PyOOPy import PyOOPy, Final

class Class(metaclass=PyOOPy):
    final_field: Final = 'final_field'

    def final_method(self) -> Final:
        return 'final_method'
```
### Abstract
```python
from PyOOPy import PyOOPy, Abstract

class Class(metaclass=PyOOPy):
    def __init__(self) -> Abstract:
        pass
```
## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
