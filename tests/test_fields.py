from test_models import base_fields, child_fields
from PyOOP import PyOOP
import pytest


# Base
def test_base_fields_protected():
    assert 'success' == base_fields.protected_field_getter()


def test_base_fields_private():
    assert 'success' == base_fields.private_field_getter()


def test_base_fields_public():
    assert 'success' == base_fields.public_field_getter()


# Child
def test_child_fields_protected():
    assert 'success' == child_fields.protected_field_getter()


def test_child_fields_private():
    with pytest.raises(PyOOP.AccessError):
        _ = child_fields.private_field_getter()


def test_child_fields_public():
    assert 'success' == child_fields.public_field_getter()


# Global
def test_global_protected():
    with pytest.raises(PyOOP.AccessError):
        _ = base_fields.protected_field


def test_global_private():
    with pytest.raises(PyOOP.AccessError):
        _ = base_fields.private_field


def test_global_public():
    assert 'success' == base_fields.public_field
