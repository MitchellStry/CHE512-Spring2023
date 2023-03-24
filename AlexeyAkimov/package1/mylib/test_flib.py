import flib
import pytest


def test_f1_1():
    """
    Testing function f1
    """
    assert flib.f1(1.0) == 1.0 

def test_f1_2():
    assert flib.f1(1) == 1


def test_f2_1():
    assert flib.f2(2) == 4  

def test_f2_2():
    assert flib.f2(2.0) == 4.0 


@pytest.mark.parametrize("x, y", [(5, 25), (10, 100), (100, 10000)])
def test_f2_many(x, y):
    assert flib.f2(x) == y  



#@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
#def test_multiplication_11(num, output):
#   assert 11*num == output
