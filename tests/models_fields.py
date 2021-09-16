from dataclasses import dataclass
from PyOOP import PyOOP


@dataclass
class Base(PyOOP):
    protected_field: PyOOP.Protected = 'success'
    private_field: PyOOP.Private = 'success'
    public_field: PyOOP.Public = 'success'

    def protected_field_getter(self):
        return self.protected_field

    def private_field_getter(self):
        return self.private_field

    def public_field_getter(self):
        return self.public_field


class Intermediate(Base):
    pass


class Child(Intermediate):
    pass


child = Child()
base = Base()
