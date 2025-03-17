from app.commands import Command
from multiprocessing import current_process

class SubtractCommand(Command):
    """Command that performs subtraction with error handling."""

    def execute(self, x, y):
        """Performs subtraction in a separate process."""
        try:
            print(f"Process {current_process().name}: Result = {x - y}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def register(handler):
    """Registers the SubtractCommand dynamically."""
    handler.register_command("subtract", SubtractCommand())
