from .default import *  # noqa

try:
    from local import *  # noqa
except ImportError as ex:
    print('error occured when import local settings', ex)
    import traceback
    traceback.print_stack()
