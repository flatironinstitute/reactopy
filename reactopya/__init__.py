from .component import Component
from .shellscript import ShellScript

def reactopya_templates_directory():
    import os
    dirname = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dirname, 'templates')