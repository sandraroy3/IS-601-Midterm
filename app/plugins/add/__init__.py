from app.commands import Command
from multiprocessing import current_process

class AddCommand(Command):
    """Command that performs addition with error handling."""

    def execute(self, x, y):
        """Performs addition in a separate process."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            print(f"Process {current_process().name}: Result = {x + y}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def register(handler):
    """Registers the AddCommand dynamically."""
    handler.register_command("add", AddCommand())