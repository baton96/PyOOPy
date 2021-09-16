# PyOOP :poop:
**P**ython **O**bject-**O**riented **P**rogramming library

## Installation
```pip install PyOOP```

## Usage
```python
from dataclasses import dataclass
from PyOOP import PyOOP

@dataclass
class Base(PyOOP):
    protected_field: PyOOP.Protected = None
    private_field: PyOOP.Private = None
    public_field: PyOOP.Public = None

    @PyOOP.protected
    def protected_method(self):
        pass

    @PyOOP.private
    def private_method(self):
        pass

    @PyOOP.public
    def public_method(self):
        pass
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
