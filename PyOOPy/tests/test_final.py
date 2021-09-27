from dataclasses import dataclass
from PyOOPy import PyOOPy, Final
import pytest


class A(PyOOPy):
    def __init__(self, final: Final = 0, nonfinal: int = 0):
        self.final = final
        self.nonfinal = nonfinal


@dataclass
class B(PyOOPy):
    final: Final = 0
    nonfinal: int = 0


@pytest.fixture
def a(): return A()


@pytest.fixture
def b(): return B()


def test_a_final_inc(a):
    with pytest.raises(AttributeError):
        a.final += 1


def test_a_final_set(a):
    with pytest.raises(AttributeError):
        a.final = 1


def test_a_nonfinal_inc(a):
    before = a.nonfinal
    a.nonfinal += 1
    after = a.nonfinal
    assert after == before + 1


def test_a_nonfinal_set(a):
    a.nonfinal = 1
    assert a.nonfinal == 1


def test_b_final_inc(b):
    with pytest.raises(AttributeError):
        b.final += 1


def test_b_final_set(b):
    with pytest.raises(AttributeError):
        b.final = 1


def test_b_nonfinal_inc(b):
    before = b.nonfinal
    b.nonfinal += 1
    after = b.nonfinal
    assert after == before + 1


def test_b_nonfinal_set(b):
    b.nonfinal = 1
    assert b.nonfinal == 1
