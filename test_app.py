
from app import greet, add_numbers

def test_greet():
    assert greet() == "Hello, DevOps World!"

def test_add_numbers():
    assert add_numbers(10, 20) == 30

def test_add_zero():
    assert add_numbers(5, 0) == 5

