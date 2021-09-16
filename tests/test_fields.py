from models_fields import base, child
from PyOOP import PyOOP
import pytest


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
    with pytest.raises(PyOOP.AccessError):
        _ = child.private_field_getter()


def test_child_public():
    assert 'success' == child.public_field_getter()


# Global
def test_global_protected():
    with pytest.raises(PyOOP.AccessError):
        _ = base.protected_field


def test_global_private():
    with pytest.raises(PyOOP.AccessError):
        _ = base.private_field


def test_global_public():
    assert 'success' == base.public_field
