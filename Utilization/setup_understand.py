"""

This is configuration file for understand path

You should set the path of understand installation in this script

"""

import os
import sys
import logging
from .constants import *

from dotenv import load_dotenv


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__file__)

load_dotenv()


# -------------------

# For Linux os

# PYTHONPATH = os.environ.get("PYTHONPATH")  # Put your path here

# In Environmnet Variables Windows Setting In System Variables Add New Setting With Varieble name PYTHONPATH and variable value C:\Program Files\SciTools\bin\pc-win64\Python

# -------------------

# For Windows os

# https://scitools.com/support/python-api/

# Python 3.8 and newer require the user add a call to os.add_dll_directory(“SciTools/bin/“  # Put your path here

# os.add_dll_directory('C:/Program Files/SciTools/bin/pc-win64')  # Put your path here
jls_extract_var = sys
jls_extract_var.path.insert(0, PYTHONPATH)  # Put your path here

os.add_dll_directory(undrestand_directory)


# --------------------

# Import understand if available on the path

try:
    import understand as und
    logger.info(f"Loaded understand {und.version()} successfully")
except ModuleNotFoundError:
    raise ModuleNotFoundError('Understand not found.')
except ImportError:
    raise ImportError("Can not import")

