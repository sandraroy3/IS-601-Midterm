from abc import ABC, abstractmethod
from multiprocessing import Process

class Command(ABC):
    """Abstract base class for all commands."""
    
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    """Handles command registration and execution dynamically using multiprocessing."""
    
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Registers a new command by name."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """
        Uses multiprocessing to execute the command in a separate process.
        Passes collected arguments to avoid EOFError when using input().
        """
        try:
            process = Process(target=self.commands[command_name].execute, args=args)
            process.start()
            process.join()  # Wait for the process to complete
        except KeyError:
            print(f"No such command: {command_name}")  # Handles cases where command does not exist