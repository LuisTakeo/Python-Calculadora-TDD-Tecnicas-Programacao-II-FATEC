import os
import sys

# Garante que a raiz do projeto esteja no sys.path para importações do pacote local
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
