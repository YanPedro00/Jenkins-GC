import pytest
from conversor import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    celsius_para_kelvin,
)


@pytest.mark.parametrize("c, f", [(0, 32), (100, 212), (-40, -40), (37, 98.6)])
def test_celsius_para_fahrenheit(c, f):
    assert celsius_para_fahrenheit(c) == pytest.approx(f)


@pytest.mark.parametrize("f, c", [(32, 0), (212, 100), (-40, -40)])
def test_fahrenheit_para_celsius(f, c):
    assert fahrenheit_para_celsius(f) == pytest.approx(c)


def test_celsius_para_kelvin():
    assert celsius_para_kelvin(0) == pytest.approx(273.15)
    assert celsius_para_kelvin(-273.15) == pytest.approx(0)
