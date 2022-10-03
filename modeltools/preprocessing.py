"""
Este módulo contiene helpers para el preprocesamiento de datos
"""

import numpy as np
from pandas import DataFrame


def get_numerical_features(df:DataFrame):
    return list(df.select_dtypes(include=[np.number]).columns)