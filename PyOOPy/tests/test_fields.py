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


@pytest.fixture
def child(): return Child()


@pytest.fixture
def base(): return Base()


# Base
def test_base_protected(base):
    assert 'success' == base.protected_field_getter()


def test_base_private(base):
    assert 'success' == base.private_field_getter()


def test_base_public(base):
    assert 'success' == base.public_field_getter()


# Child
def test_child_protected(child):
    assert 'success' == child.protected_field_getter()


def test_child_private(child):
    with pytest.raises(AttributeError):
        child.private_field_getter()


def test_child_public(child):
    assert 'success' == child.public_field_getter()


# Global
def test_global_protected(base):
    with pytest.raises(AttributeError):
        _ = base.protected_field


def test_global_private(base):
    with pytest.raises(AttributeError):
        _ = base.private_field


def test_global_public(base):
    assert 'success' == base.public_field
