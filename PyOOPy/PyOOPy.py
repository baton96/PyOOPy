from keywords import *
import sys


def method_access(obj, name):
    try:
        method = object.__getattribute__(obj, name)
        annotations = method.__annotations__
        access = annotations.get('return')
        return access
    except AttributeError:
        return


def field_access(obj, name):
    try:
        cls_annotations = object.__getattribute__(obj, '__annotations__')
    except AttributeError:
        cls_annotations = {}

    try:
        init = object.__getattribute__(obj, '__init__')
        obj_annotations = init.__annotations__
    except AttributeError:
        obj_annotations = {}

    annotations = {**obj_annotations, **cls_annotations}
    access = annotations.get(name)
    return access


def parents(obj):
    cls = object.__getattribute__(obj, '__class__')
    bases = cls.__bases__
    return bases


def access_error(name, cls, access):
    msg = f"Attribute '{name}' of object '{cls.__class__.__name__}' is {access.__name__.lower()}"
    return AttributeError(msg)


class PyOOPy:
    # Protected, Private, Public
    def __getattribute__(self, name):
        attribute = object.__getattribute__(self, name)
        access_check = method_access if callable(attribute) else field_access
        access = access_check(self, name)

        if access == Abstract:
            for parent in parents(self):
                if name in parent.__dict__:
                    raise access_error(name, self, access)

        caller = sys._getframe().f_back.f_locals.get('self')
        if access in (Private, Protected) and caller is not self:
            raise access_error(name, self, access)
        for parent in parents(self):
            if parent == PyOOPy:
                continue
            access = access_check(parent(), name)
            if parent != object and access is Private:
                raise access_error(name, self, access)
        return attribute

    # Abstract
    _abstract = True

    def __init_subclass__(cls):
        init = cls.__init__.__qualname__
        own_init = init.startswith(cls.__name__)
        try:
            return_type = cls.__init__.__annotations__.get('return')
        except AttributeError:
            return_type = None
        is_abstract = (return_type == Abstract)
        if own_init and is_abstract:
            cls._abstract = True
        else:
            cls._abstract = None

    def __new__(cls):
        if cls._abstract:
            raise TypeError(f"Can't instantiate abstract class {cls.__name__}")
        return object.__new__(cls)

    # Final
    def __setattr__(self, attr, value):
        caller = sys._getframe().f_back.f_code.co_name
        from_init = (caller == '__init__')
        if not from_init:
            is_callable = callable(self.__getattribute__(attr))
            access_check = method_access if is_callable else field_access
            access = access_check(self, attr)
            if access == Final:
                msg = f"Attribute '{attr}' of object '{self.__class__.__name__}' is final"
                raise AttributeError(msg)
        object.__setattr__(self, attr, value)
