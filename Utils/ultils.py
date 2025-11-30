import os
from pathlib import Path

def dirCleanner(dir):
    path_ = Path(dir)
    
    for x in os.listdir(dir):
        file_ = path_.joinpath(x)
        Path(file_).unlink(missing_ok=True)

import os, sys

def resource_path(relative_path):
    """Garante que o caminho funcione no Python normal e no exe do PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        # caminho temporário do PyInstaller
        base_path = sys._MEIPASS
    else:
        # caminho normal do Python
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)
