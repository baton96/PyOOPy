from PyOOPy import PyOOPy, Abstract
import pytest


class A(metaclass=PyOOPy):
    pass


class B(A):
    def __init__(self) -> Abstract:
        pass


class C(B):
    pass


def test_pyoopy():
    with pytest.raises(TypeError):
        PyOOPy()


def test_a():
    assert A()


def test_b():
    with pytest.raises(TypeError):
        B()


def test_c():
    assert C()
