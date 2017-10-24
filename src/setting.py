import os

def get_project_root_path():
    '''
    @rtype: str
    '''
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    return APP_ROOT
