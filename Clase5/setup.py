# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 02:31:34 2016

@author: Francixco
"""
 
from distutils.core import setup
import py2exe
import matplotlib
import numpy
import os
import sys

def numpy_dll_paths_fix():
    paths = set()
    np_path = numpy.__path__[0]
    for dirpath, _, filenames in os.walk(np_path):
        for item in filenames:
            if item.endswith('.dll'):
                paths.add(dirpath)

    sys.path.append(*list(paths))

#numpy_dll_paths_fix()

setup(console=['ejem 1.py'],  data_files=matplotlib.get_py2exe_datafiles())
 
 
 
""" 
#estoy funciona para interfaz 

from distutils.core import setup
import py2exe
import matplotlib
matplotlib.use('wxagg')
import os
import numpy 
import sys


def numpy_dll_paths_fix():
    paths = set()
    np_path = numpy.__path__[0]
    for dirpath, _, filenames in os.walk(np_path):
        for item in filenames:
            if item.endswith('.dll'):
                paths.add(dirpath)

    sys.path.append(*list(paths))

numpy_dll_paths_fix()

py2exe_opciones = {'py2exe': {"includes":["sip","matplotlib.backends.backend_qt4agg"] }}
script = [{"script":"7_plot_leer.py"}]

setup(console=script,data_files=matplotlib.get_py2exe_datafiles(),options=py2exe_opciones)
#windows o console
"""
