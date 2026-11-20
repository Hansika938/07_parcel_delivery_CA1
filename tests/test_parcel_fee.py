import pytest
from src.parcel_fee import delivery_fee

# Valid test cases
@pytest.mark.parametrize(("weight", "expected"),
   
    [ (1, 500),
        (500, 500),
        (1000, 500),
        (1001, 1000),
        (1500, 1000),
        (20000, 1000), ]
)
def test_delivery_fee(weight, expected):
    result = delivery_fee(weight)
    assert result == expected


# ValueError test cases
@pytest.mark.parametrize("weight",
  
    [    0,
        -1,
        20001])
def test_delivery_fee_invalid_range_raises_value_error(weight):

    with pytest.raises(ValueError):
        delivery_fee(weight)


# TypeError test cases

@pytest.mark.parametrize( "weight",
    
    [   "100",
        100.5,
        True])
def test_delivery_fee_invalid_type_raises_type_error(weight):

    with pytest.raises(TypeError):
        delivery_fee(weight)


