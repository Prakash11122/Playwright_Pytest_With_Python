import pytest

@pytest.fixture
def setup():
    print("this main function    1----")
    yield
    print("this  sub-function 3....")


def test_one(setup):
    print("this is my test one   2....")

def test_two(setup):
    print("this is my test two")

def test_three(setup):
    print("this is my test three")