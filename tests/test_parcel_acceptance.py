import pytest

from src.parcel_acceptance import is_parcel_accepted


# Valid test cases

def test_minimum_values_return_true():

    result = is_parcel_accepted(1, 1)

    assert result is True


def test_maximum_values_return_true():

    result = is_parcel_accepted(20000, 200)

    assert result is True

# Return False test cases

def test_zero_weight_returns_false():

    result = is_parcel_accepted(0, 100)

    assert result is False


def test_zero_length_returns_false():

    result = is_parcel_accepted(100, 0)

    assert result is False


def test_weight_above_limit_returns_false():

    result = is_parcel_accepted(20001, 100)

    assert result is False


def test_length_above_limit_returns_false():

    result = is_parcel_accepted(100, 201)

    assert result is False

# ValueError test cases

def test_negative_weight_raises_value_error():

    with pytest.raises(ValueError):
        is_parcel_accepted(-1, 100)


def test_negative_length_raises_value_error():

    with pytest.raises(ValueError):
        is_parcel_accepted(100, -1)

# TypeError test cases

def test_string_weight_raises_type_error():

    with pytest.raises(TypeError):
        is_parcel_accepted("100", 100)


def test_float_weight_raises_type_error():

    with pytest.raises(TypeError):
        is_parcel_accepted(100.5, 100)


def test_boolean_weight_raises_type_error():

    with pytest.raises(TypeError):
        is_parcel_accepted(True, 100)
