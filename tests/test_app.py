"""Tests for the App and Commands classes."""
import os
import pytest
import pandas as pd
from app import App
from app.commands import Command, CommandHandler
from app.plugins.add import AddCommand

class TestCommand:
    """Test the base Command class"""
    def test_command_is_abstract(self):
        """Test that Command is an abstract base class"""
        with pytest.raises(TypeError):
            Command()  # pylint: disable=abstract-class-instantiated

class TestCommandHandler:
    """Test the CommandHandler class"""
    def setup_method(self):
        """Set up test environment"""
        self.handler = CommandHandler()
        self.add_cmd = AddCommand()

    def test_register_command(self):
        """Test command registration"""
        self.handler.register_command("add", self.add_cmd)
        assert "add" in self.handler.commands
        assert self.handler.commands["add"] == self.add_cmd

    def test_execute_valid_command(self):
        """Test executing a valid command"""
        self.handler.register_command("add", self.add_cmd)
        result = self.handler.execute_command("add 5 3")
        assert result == 8

    def test_execute_unknown_command(self):
        """Test executing an unknown command"""
        result = self.handler.execute_command("unknown")
        assert "Error: Unknown command" in str(result)

    def test_execute_empty_command(self):
        """Test executing an empty command"""
        result = self.handler.execute_command("")
        assert "Please enter a command" in str(result)

    def test_execute_invalid_arguments(self):
        """Test executing a command with invalid arguments"""
        self.handler.register_command("add", self.add_cmd)
        result = self.handler.execute_command("add 1")
        assert "Error: Invalid arguments" in str(result)

class TestApp:
    """Test the App class"""
    def setup_method(self):
        """Set up test environment"""
        # Create test directories
        os.makedirs('logs', exist_ok=True)
        os.makedirs('history', exist_ok=True)
        self.app = App()
        self.history_path = 'history/command_history.csv'

    def teardown_method(self):
        """Clean up test environment"""
        # Clean up test files
        if os.path.exists(self.history_path):
            os.remove(self.history_path)

    def test_app_initialization(self):
        """Test App initialization"""
        assert self.app.command_handler is not None
        assert isinstance(self.app.command_history, pd.DataFrame)
        assert list(self.app.command_history.columns) == ["Command", "Result", "Timestamp"]

    def test_clear_history(self):
        """Test clearing command history"""
        # Add some commands
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        assert len(self.app.command_history) == 1

        # Clear history
        result = self.app.clear_history()
        assert "cleared successfully" in result
        assert len(self.app.command_history) == 0
        assert list(self.app.command_history.columns) == ["Command", "Result", "Timestamp"]

        # Verify file is cleared
        assert os.path.exists(self.history_path)
        df = pd.read_csv(self.history_path)
        assert len(df) == 0

    def test_delete_history_record(self):
        """Test deleting a specific history record"""
        # Add some commands
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        self.app.execute_command("add 2 4")
        assert len(self.app.command_history) == 2

        # Test invalid index
        result = self.app.delete_history_record(-1)
        assert "Invalid command index" in result
        assert len(self.app.command_history) == 2

        result = self.app.delete_history_record(2)
        assert "Invalid command index" in result
        assert len(self.app.command_history) == 2

        # Test invalid format
        result = self.app.delete_history_record("abc")
        assert "Invalid index format" in result
        assert len(self.app.command_history) == 2

        # Delete first record
        result = self.app.delete_history_record(0)
        assert "Deleted command" in result
        assert len(self.app.command_history) == 1
        assert "6" in str(self.app.command_history.iloc[0]["Result"])

        # Verify file is updated
        df = pd.read_csv(self.history_path)
        assert len(df) == 1
        assert "6" in str(df.iloc[0]["Result"])

    def test_history_persistence(self):
        """Test that command history is saved and loaded correctly"""
        # Add some commands
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        # Create new app instance to test loading
        new_app = App()
        assert len(new_app.command_history) == 1
        assert "8" in str(new_app.command_history.iloc[0]["Result"])

    def test_load_plugins(self):
        """Test plugin loading"""
        self.app.load_plugins()
        # Check if basic commands are registered
        assert "add" in self.app.command_handler.commands
        assert "menu" in self.app.command_handler.commands
        assert "greet" in self.app.command_handler.commands

    def test_execute_command_updates_history(self):
        """Test that executing a command updates history"""
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        assert len(self.app.command_history) == 1
        last_entry = self.app.command_history.iloc[-1]
        assert last_entry["Command"] == "add 5 3"
        assert "8" in str(last_entry["Result"])
        assert pd.notna(last_entry["Timestamp"])

    def test_clear_history_command(self):
        """Test clear_history command"""
        # Add some commands
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        assert len(self.app.command_history) == 1

        # Clear history using command
        result = self.app.execute_command("clear_history")
        assert "cleared successfully" in result
        assert len(self.app.command_history) == 0

    def test_delete_history_command(self):
        """Test delete_history command"""
        # Add some commands
        self.app.command_handler.register_command("add", AddCommand())
        self.app.execute_command("add 5 3")
        self.app.execute_command("add 2 4")
        assert len(self.app.command_history) == 2

        # Test missing index
        result = self.app.execute_command("delete_history")
        assert "requires an index argument" in result
        assert len(self.app.command_history) == 2

        # Test invalid index
        result = self.app.execute_command("delete_history -1")
        assert "Invalid command index" in result
        assert len(self.app.command_history) == 2

        # Test out of range index
        result = self.app.execute_command("delete_history 2")
        assert "Invalid command index" in result
        assert len(self.app.command_history) == 2

        # Test invalid format
        result = self.app.execute_command("delete_history abc")
        assert "Invalid index format" in result
        assert len(self.app.command_history) == 2

        # Delete first record
        result = self.app.execute_command("delete_history 0")
        assert "Deleted command" in result
        assert len(self.app.command_history) == 1
        assert "6" in str(self.app.command_history.iloc[0]["Result"])
