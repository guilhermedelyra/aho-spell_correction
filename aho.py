# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_aho')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_aho')
    _aho = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_aho', [dirname(__file__)])
        except ImportError:
            import _aho
            return _aho
        try:
            _mod = imp.load_module('_aho', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _aho = swig_import_helper()
    del swig_import_helper
else:
    import _aho
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _aho.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _aho.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _aho.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _aho.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _aho.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _aho.SwigPyIterator_equal(self, x)

    def copy(self):
        return _aho.SwigPyIterator_copy(self)

    def next(self):
        return _aho.SwigPyIterator_next(self)

    def __next__(self):
        return _aho.SwigPyIterator___next__(self)

    def previous(self):
        return _aho.SwigPyIterator_previous(self)

    def advance(self, n):
        return _aho.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _aho.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _aho.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _aho.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _aho.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _aho.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _aho.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _aho.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vs(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vs, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vs, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _aho.vs_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _aho.vs___nonzero__(self)

    def __bool__(self):
        return _aho.vs___bool__(self)

    def __len__(self):
        return _aho.vs___len__(self)

    def __getslice__(self, i, j):
        return _aho.vs___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _aho.vs___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _aho.vs___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _aho.vs___delitem__(self, *args)

    def __getitem__(self, *args):
        return _aho.vs___getitem__(self, *args)

    def __setitem__(self, *args):
        return _aho.vs___setitem__(self, *args)

    def pop(self):
        return _aho.vs_pop(self)

    def append(self, x):
        return _aho.vs_append(self, x)

    def empty(self):
        return _aho.vs_empty(self)

    def size(self):
        return _aho.vs_size(self)

    def swap(self, v):
        return _aho.vs_swap(self, v)

    def begin(self):
        return _aho.vs_begin(self)

    def end(self):
        return _aho.vs_end(self)

    def rbegin(self):
        return _aho.vs_rbegin(self)

    def rend(self):
        return _aho.vs_rend(self)

    def clear(self):
        return _aho.vs_clear(self)

    def get_allocator(self):
        return _aho.vs_get_allocator(self)

    def pop_back(self):
        return _aho.vs_pop_back(self)

    def erase(self, *args):
        return _aho.vs_erase(self, *args)

    def __init__(self, *args):
        this = _aho.new_vs(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _aho.vs_push_back(self, x)

    def front(self):
        return _aho.vs_front(self)

    def back(self):
        return _aho.vs_back(self)

    def assign(self, n, x):
        return _aho.vs_assign(self, n, x)

    def resize(self, *args):
        return _aho.vs_resize(self, *args)

    def insert(self, *args):
        return _aho.vs_insert(self, *args)

    def reserve(self, n):
        return _aho.vs_reserve(self, n)

    def capacity(self):
        return _aho.vs_capacity(self)
    __swig_destroy__ = _aho.delete_vs
    __del__ = lambda self: None
vs_swigregister = _aho.vs_swigregister
vs_swigregister(vs)

class vi(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vi, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vi, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _aho.vi_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _aho.vi___nonzero__(self)

    def __bool__(self):
        return _aho.vi___bool__(self)

    def __len__(self):
        return _aho.vi___len__(self)

    def __getslice__(self, i, j):
        return _aho.vi___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _aho.vi___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _aho.vi___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _aho.vi___delitem__(self, *args)

    def __getitem__(self, *args):
        return _aho.vi___getitem__(self, *args)

    def __setitem__(self, *args):
        return _aho.vi___setitem__(self, *args)

    def pop(self):
        return _aho.vi_pop(self)

    def append(self, x):
        return _aho.vi_append(self, x)

    def empty(self):
        return _aho.vi_empty(self)

    def size(self):
        return _aho.vi_size(self)

    def swap(self, v):
        return _aho.vi_swap(self, v)

    def begin(self):
        return _aho.vi_begin(self)

    def end(self):
        return _aho.vi_end(self)

    def rbegin(self):
        return _aho.vi_rbegin(self)

    def rend(self):
        return _aho.vi_rend(self)

    def clear(self):
        return _aho.vi_clear(self)

    def get_allocator(self):
        return _aho.vi_get_allocator(self)

    def pop_back(self):
        return _aho.vi_pop_back(self)

    def erase(self, *args):
        return _aho.vi_erase(self, *args)

    def __init__(self, *args):
        this = _aho.new_vi(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _aho.vi_push_back(self, x)

    def front(self):
        return _aho.vi_front(self)

    def back(self):
        return _aho.vi_back(self)

    def assign(self, n, x):
        return _aho.vi_assign(self, n, x)

    def resize(self, *args):
        return _aho.vi_resize(self, *args)

    def insert(self, *args):
        return _aho.vi_insert(self, *args)

    def reserve(self, n):
        return _aho.vi_reserve(self, n)

    def capacity(self):
        return _aho.vi_capacity(self)
    __swig_destroy__ = _aho.delete_vi
    __del__ = lambda self: None
vi_swigregister = _aho.vi_swigregister
vi_swigregister(vi)

class msvi(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, msvi, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, msvi, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _aho.msvi_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _aho.msvi___nonzero__(self)

    def __bool__(self):
        return _aho.msvi___bool__(self)

    def __len__(self):
        return _aho.msvi___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _aho.msvi___getitem__(self, key)

    def __delitem__(self, key):
        return _aho.msvi___delitem__(self, key)

    def has_key(self, key):
        return _aho.msvi_has_key(self, key)

    def keys(self):
        return _aho.msvi_keys(self)

    def values(self):
        return _aho.msvi_values(self)

    def items(self):
        return _aho.msvi_items(self)

    def __contains__(self, key):
        return _aho.msvi___contains__(self, key)

    def key_iterator(self):
        return _aho.msvi_key_iterator(self)

    def value_iterator(self):
        return _aho.msvi_value_iterator(self)

    def __setitem__(self, *args):
        return _aho.msvi___setitem__(self, *args)

    def asdict(self):
        return _aho.msvi_asdict(self)

    def __init__(self, *args):
        this = _aho.new_msvi(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _aho.msvi_empty(self)

    def size(self):
        return _aho.msvi_size(self)

    def swap(self, v):
        return _aho.msvi_swap(self, v)

    def begin(self):
        return _aho.msvi_begin(self)

    def end(self):
        return _aho.msvi_end(self)

    def rbegin(self):
        return _aho.msvi_rbegin(self)

    def rend(self):
        return _aho.msvi_rend(self)

    def clear(self):
        return _aho.msvi_clear(self)

    def get_allocator(self):
        return _aho.msvi_get_allocator(self)

    def count(self, x):
        return _aho.msvi_count(self, x)

    def erase(self, *args):
        return _aho.msvi_erase(self, *args)

    def find(self, x):
        return _aho.msvi_find(self, x)

    def lower_bound(self, x):
        return _aho.msvi_lower_bound(self, x)

    def upper_bound(self, x):
        return _aho.msvi_upper_bound(self, x)
    __swig_destroy__ = _aho.delete_msvi
    __del__ = lambda self: None
msvi_swigregister = _aho.msvi_swigregister
msvi_swigregister(msvi)


def buildMatchingMachine(words, f, g, out):
    return _aho.buildMatchingMachine(words, f, g, out)
buildMatchingMachine = _aho.buildMatchingMachine

def findNextState(currentState, nextInput, f, g):
    return _aho.findNextState(currentState, nextInput, f, g)
findNextState = _aho.findNextState

def search(keywords, text):
    return _aho.search(keywords, text)
search = _aho.search
# This file is compatible with both classic and new-style classes.


