import pytest

from calculator import add, subtract, multiply, divide

def test add(:
  assert add(2,3) == 3
def test subtract():
  assert subtract (10, 4) == 6
def test multiply():
  assert multiply(3, 5) == 15
def test divide():
  assert divide(10, 4) == 2.5
def test divide by zero():
  with pytest.raisesV(alueError):
    divide(1, 0)
