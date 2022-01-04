import inspect

Protected = type('Protected', (), {})
Private = type('Private', (), {})
Public = type('Public', (), {})
Abstract = type('Abstract', (), {})
Final = type('Final', (), {})


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


class PyOOPy(type):
    def __init__(cls, what, bases, attr_dict):
        super().__init__(what, bases, attr_dict)

        try:
            annotations = cls.__init__.__annotations__
        except AttributeError:
            annotations = {}
        return_type = annotations.get('return')

        # General case
        if return_type:
            if not hasattr(cls, '__annotations__'):
                cls.__annotations__ = {}

            arg_names = inspect.getfullargspec(cls.__init__).args[1:]
            for name in arg_names:
                annotations.setdefault(name, return_type)

            attribute_names = [attribute for attribute in cls.__dict__.keys() if attribute[0] != '_']
            for name in attribute_names:
                attribute = object.__getattribute__(cls, name)
                if callable(attribute):
                    attribute.__annotations__.setdefault('return', return_type)
                else:
                    cls.__annotations__.setdefault(name, return_type)

        def __init_subclass__(decorated_class):
            try:
                init_annotations = decorated_class.__init__.__annotations__
            except AttributeError:
                init_annotations = {}
            return_annotation = init_annotations.get('return')

            # Abstract class
            init = decorated_class.__init__.__qualname__
            own_init = init.startswith(decorated_class.__name__)
            if own_init and return_annotation == Abstract:
                decorated_class._abstract = True
            else:
                decorated_class._abstract = None

        cls.__init_subclass__ = classmethod(__init_subclass__)

        def __getattribute__(self, attr_name):
            attribute = object.__getattribute__(self, attr_name)
            access_check = method_access if callable(attribute) else field_access
            access = access_check(self, attr_name)

            if access == Abstract:
                for parent in parents(self):
                    if parent == PyOOPy:
                        continue
                    parent_access = access_check(parent(), attr_name)
                    if parent_access is Abstract:
                        break
                else:
                    raise access_error(attr_name, self, access)

            caller = inspect.currentframe().f_back.f_locals.get('self')
            if access in (Private, Protected) and caller is not self:
                raise access_error(attr_name, self, access)
            for parent in parents(self):
                if parent == PyOOPy:
                    continue
                access = access_check(parent(), attr_name)
                if access is Private:
                    raise access_error(attr_name, self, access)
            return attribute

        cls.__getattribute__ = __getattribute__

        def __new__(cls2):
            if getattr(cls2, '_abstract', False):
                raise TypeError(f"Can't instantiate abstract class {cls2.__name__}")
            return object.__new__(cls2)

        cls.__new__ = __new__

        def __setattr__(self, attr_name, value):
            caller = inspect.currentframe().f_back.f_code.co_name
            from_init = (caller == '__init__')
            if not from_init:
                if attr_name in dir(self):
                    attribute = object.__getattribute__(self, attr_name)
                    access_check = method_access if callable(attribute) else field_access
                    access = access_check(self, attr_name)
                    if access == Final:
                        msg = f"Attribute '{attr_name}' of object '{self.__class__.__name__}' is final"
                        raise AttributeError(msg)
                else:
                    try:
                        cls_access = self.__init__.__annotations__.get('return')
                    except AttributeError:
                        cls_access = None
                    if cls_access == Final:
                        msg = f"Class '{self.__class__.__name__}' is final"
                        raise TypeError(msg)
            object.__setattr__(self, attr_name, value)

        cls.__setattr__ = __setattr__
