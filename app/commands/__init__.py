from abc import ABC, abstractmethod
from multiprocessing import Process

class Command(ABC):
    """Abstract base class for all commands."""
    
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, cmd_input):
        """Executes a registered command with arguments"""
        parts = cmd_input.split()  # Split user input into parts
        cmd_name = parts[0].lower()  # Command name (first word)
        args = parts[1:]  # Remaining words as arguments

        # LBYL approach - commented out
        # if cmd_name in self.commands:
        #     try:
        #         result = self.commands[cmd_name].execute(*args)  # Pass arguments
        #         if result is not None:
        #             print(result)  # Print command output
        #     except TypeError as e:
        #         print(f"Error: Invalid arguments for '{cmd_name}' command. {e}")
        # else:
        #     print(f"Error: Unknown command '{cmd_name}'.")

        # EAFP approach - recommended way
        try:
            result = self.commands[cmd_name].execute(*args)  # Attempt to execute command
            if result is not None:
                print(result)  # Print command output
        except KeyError:
            print(f"Error: Unknown command '{cmd_name}'.")
        except TypeError as e:
            print(f"Error: Invalid arguments for '{cmd_name}' command. {e}")