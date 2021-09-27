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


class Protected:
    pass


class Private:
    pass


class Public:
    pass


class PyOOPy:
    def __getattribute__(self, name):
        attribute = object.__getattribute__(self, name)
        caller = inspect.currentframe().f_back.f_locals.get('self')
        access_check = method_access if callable(attribute) else field_access
        access = access_check(self, name)
        if access in (Private, Protected) and caller is not self:
            raise access_error(name, self, access)
        for parent in parents(self):
            access = access_check(parent(), name)
            if parent != object and access is Private:
                raise access_error(name, self, access)
        return attribute
