import os
import sys
sys.path.append(os.path.dirname(__file__))
try:
    from . import rss_reader
except ImportError as e:
    raise ImportError(e)