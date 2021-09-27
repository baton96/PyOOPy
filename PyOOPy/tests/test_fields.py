from PyOOPy import PyOOPy, Protected, Private, Public
from dataclasses import dataclass
import pytest


@dataclass
class Base(PyOOPy):
    protected_field: Protected = 'success'
    private_field: Private = 'success'
    public_field: Public = 'success'

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


# Base
def test_base_protected():
    assert 'success' == base.protected_field_getter()


def test_base_private():
    assert 'success' == base.private_field_getter()


def test_base_public():
    assert 'success' == base.public_field_getter()


# Child
def test_child_protected():
    assert 'success' == child.protected_field_getter()


def test_child_private():
    with pytest.raises(PyOOPy.AccessError):
        _ = child.private_field_getter()


def test_child_public():
    assert 'success' == child.public_field_getter()


# Global
def test_global_protected():
    with pytest.raises(PyOOPy.AccessError):
        _ = base.protected_field


def test_global_private():
    with pytest.raises(PyOOPy.AccessError):
        _ = base.private_field


def test_global_public():
    assert 'success' == base.public_field
