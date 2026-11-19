import pytest
from Src.parcel_fee import delivery_fee

# Valid test cases

def test_weightgrams_1_returns_500():

    # Arrange
    weight = 1

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 500


def test_weightgrams_500_returns_500():

    # Arrange
    weight = 500

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 500


def test_weightgrams_1000_returns_500():

    # Arrange
    weight = 1000

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 500


def test_weightgrams_1001_returns_1000():

    # Arrange
    weight = 1001

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 1000


def test_weightgrams_1500_returns_1000():

    # Arrange
    weight = 1500

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 1000


def test_weightgrams_20000_returns_1000():

    # Arrange
    weight = 20000

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == 1000


# ValueError test cases

def test_weightgrams_0_raises_value_error():

    with pytest.raises(ValueError):
        delivery_fee(0)


def test_weightgrams_negative_raises_value_error():

    with pytest.raises(ValueError):
        delivery_fee(-1)


def test_weightgrams_20001_raises_value_error():

    with pytest.raises(ValueError):
        delivery_fee(20001)
# TypeError test cases

def test_string_weight_raises_type_error():

    with pytest.raises(TypeError):
        delivery_fee("100")


def test_float_weight_raises_type_error():

    with pytest.raises(TypeError):
        delivery_fee(100.5)


def test_boolean_weight_raises_type_error():

    with pytest.raises(TypeError):
        delivery_fee(True)

