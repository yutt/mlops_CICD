import pandas as pd
import pytest
from modeltools.preprocessing import get_numerical_features

def test_prepytestprocessing_simple():
    """
    test
    """
    
    df = pd.DataFrame({
        'numerica':[5],
        'categorica':["rojo"]
    })
    assert get_numerical_features(df) == ['numerica']


def test_get_numerical_features_empty():

    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""
    df =  pd.DataFrame({
        #'numerica':[5],
        'categorica':["rojo"]
    })
    assert get_numerical_features(df) == []
    



def test_get_numerical_features_zero_columns():

    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""
    df =  pd.DataFrame()
    assert get_numerical_features(df) == []
    

def test_get_numerical_features_int_and_float():

    """Este test comprueba que funciona correctamente

    cuando hay una columna integer y una flotante"""
    df =  pd.DataFrame({
        'numerica1':[5],
        'numerica2':[.5]
    })
    assert get_numerical_features(df) == [ 'numerica1','numerica2']
    