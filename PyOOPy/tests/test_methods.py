from dataclasses import dataclass
from PyOOPy import PyOOPy
import pytest


@dataclass
class Base(PyOOPy):
    @PyOOPy.protected
    def protected_method(self):
        return 'success'

    @PyOOPy.private
    def private_method(self):
        return 'success'

    @PyOOPy.public
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


# Base
def test_base_protected():
    assert 'success' == base.protected_method_getter()


def test_base_private():
    assert 'success' == base.private_method_getter()


def test_base_public():
    assert 'success' == base.public_method_getter()


# Child
def test_child_protected():
    assert 'success' == child.protected_method_getter()


def test_child_private():
    with pytest.raises(PyOOPy.AccessError):
        _ = child.private_method_getter()


def test_child_public():
    assert 'success' == child.public_method_getter()


# Global
def test_global_protected():
    with pytest.raises(PyOOPy.AccessError):
        _ = base.protected_method()


def test_global_private():
    with pytest.raises(PyOOPy.AccessError):
        _ = base.private_method()


def test_global_public():
    assert 'success' == base.public_method()
