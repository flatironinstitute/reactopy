####################################################################
## This file is automatically generated
## Do not edit manually
####################################################################

from .all_widgets import *

from ._version import __version__

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': '{{ extension_name }}_jup',
        'require': '{{ extension_name }}_jup/extension'
    }]
