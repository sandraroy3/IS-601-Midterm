"""Tests for calculator plugin functionality."""
import pandas as pd
from app import App
from app.commands import CommandHandler
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.greet import GreetCommand
from app.plugins.menu import MenuCommand

def test_add():
    """Test AddCommand with various scenarios"""
    command = AddCommand()
    # Test normal addition
    assert command.execute(5, 5) == 10
    assert command.execute(-1, 1) == 0
    # Test invalid input
    assert "Invalid input" in command.execute("abc", "def")

def test_subtract():
    """Test SubtractCommand with various scenarios"""
    command = SubtractCommand()
    # Test normal subtraction
    assert command.execute(5, 3) == 2
    assert command.execute(0, 5) == -5
    # Test invalid input
    assert "Invalid input" in command.execute("abc", "def")

def test_multiply():
    """Test MultiplyCommand with various scenarios"""
    command = MultiplyCommand()
    # Test normal multiplication
    assert command.execute(5, 3) == 15
    assert command.execute(-2, 3) == -6
    # Test invalid input
    assert "Invalid input" in command.execute("abc", "def")

def test_divide():
    """Test DivideCommand with various scenarios"""
    command = DivideCommand()
    # Test normal division
    assert command.execute(10, 2) == 5
    assert command.execute(-6, 2) == -3
    # Test division by zero
    assert "Division by zero" in command.execute(5, 0)
    # Test invalid input
    assert "Invalid input" in command.execute("abc", "def")

def test_greet():
    """Test GreetCommand"""
    command = GreetCommand()
    result = command.execute()
    assert "Hello, World!" in result

def test_menu():
    """Test MenuCommand"""
    handler = CommandHandler()
    command = MenuCommand(handler)
    result = command.execute()
    assert "Available commands" in result

def test_command_handler():
    """Test CommandHandler functionality"""
    handler = CommandHandler()
    # Test empty command
    assert "Please enter a command" in handler.execute_command("")
    # Test unknown command
    assert "Error: Unknown command" in handler.execute_command("unknown")
    # Test invalid arguments
    handler.register_command("add", AddCommand())
    assert "Error: Invalid arguments" in handler.execute_command("add 1")

def test_command_history():
    """Test command history functionality"""
    app = App()
    # Clear history
    app.command_history = pd.DataFrame(columns=["Command", "Result", "Timestamp"])
    # Register commands
    app.command_handler.register_command("add", AddCommand())
    app.command_handler.register_command("divide", DivideCommand())
    # Execute commands through app to update history
    app.execute_command("add 5 3")
    app.execute_command("divide 6 0")
    # Check history DataFrame
    assert len(app.command_history) == 2
    assert "8" in str(app.command_history.iloc[0]["Result"])
    assert "Division by zero" in str(app.command_history.iloc[1]["Result"])

def test_error_handling():
    """Test various error scenarios"""
    handler = CommandHandler()
    handler.register_command("divide", DivideCommand())
    handler.register_command("add", AddCommand())
    # Test division by zero
    result = handler.execute_command("divide 5 0")
    assert "Division by zero" in str(result)
    # Test invalid input
    result = handler.execute_command("add abc def")
    assert "Invalid input" in str(result)
    # Test empty command
    result = handler.execute_command("")
    assert "Please enter a command" in str(result)
    # Test unknown command
    result = handler.execute_command("unknown")
    assert "Error: Unknown command" in str(result)
