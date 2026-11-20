import pytest

from src.parcel_acceptance import is_parcel_accepted


# Valid test cases
@pytest.mark.parametrize("weight, length",
                          [(1, 1),(20000,200),])

def test_valid_parcel_acceptance(weight, length):
    result = is_parcel_accepted(weight, length)
    assert result is True 

# Return False test cases
@pytest.mark.parametrize("weight, length",
                         [(0,150),(150,0),(20001,150),(150,201),])


def test_invalid_parcel_acceptance(weight, length):
    result = is_parcel_accepted(weight, length)
    assert result is False
 

# ValueError test cases

@pytest.mark.parametrize("weight, length",
                          [(-1, 100),(100, -1),])

def test_invalid_parcel_acceptance_raises_value_error(weight, length):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight, length)

# TypeError test cases
@pytest.mark.parametrize("weight, length",
                            [("100", 100),(100, "100"),(100.5, 100),(100, 100.5),(True, 100),(100, True),])

def test_invalid_parcel_acceptance_raises_type_error(weight, length):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight, length)
        


