'''
IO subpackage

This allows users to access the functions in the package

'''

# hi folks this is __init__.py

# this allows the user to do the function call as follows:
# molecool.io.open_pdb
from .pdb import open_pdb

from .xyz import open_xyz, write_xyz

