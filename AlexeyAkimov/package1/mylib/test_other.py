import pytest

def true_or_false(x):
    return x


@pytest.mark.parametrize("x, y", [(True, True), (False, False)])
def test_torf(x, y):
    assert true_or_false(x) == y  
