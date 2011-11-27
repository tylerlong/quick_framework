# coding=utf-8
"""
    quick
    ~~~~~
    core file for quick framework
"""
import os, sys
from toolkit_library.inspector import ModuleInspector
from toolkit_library.input_util import InputUtil

def create_project():
    """Create a new project"""
    project_name = InputUtil.get_input('project name', default = 'test', pattern = '[a-z][a-z_]{,63}')
    if os.path.exists(project_name):
        if os.path.isdir(project_name):
            print 'a folder with the same name already exists in the current directory'
        else:
            print 'a file with the same name already exists in the current directory'
        return
    os.makedirs(project_name)
    print 'project {0} created'.format(project_name)
    

if __name__ == '__main__':
    inspector = ModuleInspector(sys.modules[__name__])
    inspector.invoke(*sys.argv[1:])
