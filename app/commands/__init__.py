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
        parts = cmd_input.strip().split()  # Split user input into parts
        
        # Handle empty input
        if not parts:
            msg = "Please enter a command. Type 'menu' for available commands."
            print(msg)
            return msg
            
        cmd_name = parts[0].lower()  # Command name (first word)
        args = parts[1:]  # Remaining words as arguments


        # Look Before You Leap (LBYL)
        # if cmd_name not in self.commands:
        #     error_msg = f"Error: Unknown command '{cmd_name}'"
        #     print(error_msg)
        #     return error_msg

        # command = self.commands[cmd_name]
        
        # if not callable(getattr(command, "execute", None)):
        #     error_msg = f"Error: Command '{cmd_name}' does not have a valid execute method."
        #     print(error_msg)
        #     return error_msg

        # try:
        #     result = command.execute(*args)
        #     return result if result is not None else "Command executed with no result"
        # except TypeError as e:
        #     error_msg = f"Error: Invalid arguments for '{cmd_name}' command. {e}"
        #     print(error_msg)
        #     return error_msg

        # Easier to ask for Permission than for Forgiveness (EAPF)
        try:
            result = self.commands[cmd_name].execute(*args)  # Attempt to execute command
            # Return the result even if it's None or an error message
            return result if result is not None else "Command executed with no result"
        except KeyError:
            error_msg = f"Error: Unknown command '{cmd_name}'"
            print(error_msg)
            return error_msg
        except TypeError as e:
            error_msg = f"Error: Invalid arguments for '{cmd_name}' command. {e}"
            print(error_msg)
            return error_msg