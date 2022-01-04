from PyOOPy import PyOOPy, Abstract
from dataclasses import dataclass
import pytest


@dataclass
class Base(metaclass=PyOOPy):
    field: Abstract = 'success'

    def method(self) -> Abstract:
        return 'success'


class Intermediate(Base):
    pass


class Child(Intermediate):
    pass


@pytest.fixture
def child(): return Child()


@pytest.fixture
def base(): return Base()


def test_base_field(base):
    with pytest.raises(AttributeError):
        _ = base.field


def test_base_method(base):
    with pytest.raises(AttributeError):
        base.method()


def test_child_field(child):
    assert 'success' == child.field


def test_child_method(child):
    assert 'success' == child.method()
