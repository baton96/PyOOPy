import inspect


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
        init = object.__getattribute__(obj, '__init__')
        annotations = init.__annotations__
        access = annotations.get(name)
        return access
    except AttributeError:
        return


def parents(obj):
    cls = object.__getattribute__(obj, '__class__')
    bases = cls.__bases__
    return bases


class Protected:
    pass


class Private:
    pass


class Public:
    pass


class PyOOPy:
    class AccessError(AttributeError):
        def __init__(self, cls, attr_name, access):
            msg = f"Attribute '{attr_name}' of object '{cls.__class__.__name__}' is {access.__name__.lower()}"
            super().__init__(msg)

    def __getattribute__(self, name):
        attribute = object.__getattribute__(self, name)
        caller = inspect.currentframe().f_back.f_locals.get('self')
        access_check = method_access if callable(attribute) else field_access
        access = access_check(self, name)
        if access in (Private, Protected) and caller is not self:
            raise self.AccessError(self, name, access)
        for parent in parents(self):
            access = access_check(parent(), name)
            if parent != object and access is Private:
                raise self.AccessError(self, name, access)
        return attribute
