from geo_calculator.calculations import find_average
from geo_calculator.gardner import gardners_equation
import pytest

def test_length_of_string() -> None:
    test_string = "python"

    length = len(test_string)

    assert length == 6


def test_find_average_given_list_of_numbers() -> None:
    input_numbers = [1, 2, 3, 4, 5, 6]

    result = find_average(input_numbers)

    assert result == 3.5

def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    assert gardners_equation(velocity) == pytest.approx(expected_density)

def test_gardners_equation_negative_velocity() -> None:
    velocity = -1000  # m/s
    with pytest.raises(ValueError) as e:
        gardners_equation(velocity)