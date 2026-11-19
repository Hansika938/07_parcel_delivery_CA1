import pytest

from src.parcel_acceptance import is_parcel_accepted


# Valid test cases

def test_minimum_values_return_true():

    result = is_parcel_accepted(1, 1)

    assert result is True


def test_maximum_values_return_true():

    result = is_parcel_accepted(20000, 200)

    assert result is True
    