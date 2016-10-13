from .default import *  # noqa

try:
    from local import *  # noqa
except ImportError:
    pass
