from dataclasses import dataclass
from PyOOPy import PyOOPy, Final
import pytest


class A(metaclass=PyOOPy):
    def __init__(self, final: Final = 0, nonfinal: int = 0):
        self.final = final
        self.nonfinal = nonfinal


@dataclass
class B(metaclass=PyOOPy):
    final: Final = 0
    nonfinal: int = 0


class C(metaclass=PyOOPy):
    def final(self) -> Final:
        pass

    def nonfinal(self):
        pass


class D(metaclass=PyOOPy):
    final = 0
    nonfinal: int = 0

    def __init__(self) -> Final:
        pass


@pytest.fixture
def c():
    return C()


@pytest.fixture
def d():
    return D()


@pytest.mark.parametrize('obj', [A(), B()])
class TestFinal:
    def test_final_inc(self, obj):
        with pytest.raises(AttributeError):
            obj.final += 1

    def test_final_set(self, obj):
        with pytest.raises(AttributeError):
            obj.final = 1

    def test_nonfinal_inc(self, obj):
        before = obj.nonfinal
        obj.nonfinal += 1
        after = obj.nonfinal
        assert after == before + 1

    def test_nonfinal_set(self, obj):
        obj.nonfinal = 1
        assert obj.nonfinal == 1


def test_final_set(c):
    with pytest.raises(AttributeError):
        c.final = 1


def test_nonfinal_set(c):
    c.nonfinal = 1
    assert c.nonfinal == 1


def test_class_final_field(d):
    with pytest.raises(AttributeError):
        d.final = 1


def test_class_nonfinal_field(c):
    d.nonfinal = 1
    assert d.nonfinal == 1


def test_class_new_field(d):
    with pytest.raises(TypeError):
        d.new = 1
