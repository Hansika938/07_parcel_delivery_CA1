import pytest
from src.parcel_fee import delivery_fees

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

