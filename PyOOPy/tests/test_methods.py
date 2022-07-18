from PyOOPy import PyOOPy, Protected, Private, Public
from dataclasses import dataclass
import pytest


@dataclass
class Base(metaclass=PyOOPy):
    def protected_method(self) -> Protected[str]:
        return 'success'

    def private_method(self) -> Private[str]:
        return 'success'

    def public_method(self) -> Public[str]:
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


@pytest.fixture
def child(): return Child()


@pytest.fixture
def base(): return Base()


# Base
def test_base_protected(base):
    assert 'success' == base.protected_method_getter()


def test_base_private(base):
    assert 'success' == base.private_method_getter()


def test_base_public(base):
    assert 'success' == base.public_method_getter()


# Child
def test_child_protected(child):
    assert 'success' == child.protected_method_getter()


def test_child_private(child):
    with pytest.raises(AttributeError):
        child.private_method_getter()


def test_child_public(child):
    assert 'success' == child.public_method_getter()


# Global
def test_global_protected(base):
    with pytest.raises(AttributeError):
        base.protected_method()


def test_global_private(base):
    with pytest.raises(AttributeError):
        base.private_method()


def test_global_public(base):
    assert 'success' == base.public_method()
