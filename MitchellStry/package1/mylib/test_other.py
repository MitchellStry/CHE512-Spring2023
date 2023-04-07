import pytest
import flib
def test_f1():
    """Testing function f1"""
    print("Det")
    assert flib.f1(1.0)==1.0
def test_f1_2():
    assert flib.f1(1)==1
def test_f2_1():
    assert flib.f2(2)==4
def test_f2_2():
    assert flib.f2(2.0)==4.0
def true_or_false(x):
    return(x**2)

@pytest.mark.parametrize("x,y", [(5,25),(10,100),(100,10000)])
def test_f2_many(x,y):
    assert flib.f2(x)==y
@pytest.mark.parametrize("x,y", [(5,25),(10,100),(100,10000)])
def test_torf_many(x,y):
    assert true_or_false(x)==y
