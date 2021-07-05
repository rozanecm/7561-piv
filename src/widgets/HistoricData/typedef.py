from PyQt5.QtChart import QSplineSeries
from typing_extensions import TypedDict

line = TypedDict('line', {'is_visible': bool, 'series': QSplineSeries})
