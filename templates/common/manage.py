"""
    manage
    ~~~~~~
    This file is used to manage the project
"""
import sys
from toolkit_library.inspector import ModuleInspector


def install_requirements():
    """Install required Python packages"""
    import subprocess
    subprocess.call('pip install -r requirements.txt')


if __name__ == '__main__':
    inspector = ModuleInspector(sys.modules[__name__])
    inspector.invoke(*sys.argv[1:])
