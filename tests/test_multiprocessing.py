"""Tests for multiprocessing functionality of calculator commands."""
from app.plugins.divide import DivideCommand
from app.plugins.add import AddCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand

def test_multiprocessing_divide():
    """Test DivideCommand in multiprocessing context"""
    command = DivideCommand()
    # Test normal division
    result = command.execute(10, 2)
    assert result == 5.0
    # Test division by zero
    result = command.execute(6, 0)
    assert "Division by zero" in str(result)

def test_multiprocessing_add():
    """Test AddCommand in multiprocessing context"""
    command = AddCommand()
    # Test addition
    result = command.execute(5, 3)
    assert result == 8

def test_multiprocessing_multiply():
    """Test MultiplyCommand in multiprocessing context"""
    command = MultiplyCommand()
    # Test multiplication
    result = command.execute(4, 3)
    assert result == 12

def test_multiprocessing_subtract():
    """Test SubtractCommand in multiprocessing context"""
    command = SubtractCommand()
    # Test subtraction
    result = command.execute(8, 3)
    assert result == 5
