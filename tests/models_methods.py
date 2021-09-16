from dataclasses import dataclass
from PyOOP import PyOOP


@dataclass
class Base(PyOOP):
    @PyOOP.protected
    def protected_method(self):
        return 'success'

    @PyOOP.private
    def private_method(self):        return 'success'

    @PyOOP.public
    def public_method(self):
        return 'success'

    def protected_method_getter(self):
        return self.protected_method()

    def private_method_getter(self):
        return self.private_method()

    def public_method_getter(self):
        return self.public_method()


class Intermediate(Base):
    pass


class Child(Intermediate):
    pass


child = Child()
base = Base()
