from app.commands import Command
from multiprocessing import current_process

class MultiplyCommand(Command):
    """Command that performs multiplication with error handling."""

    def execute(self, x, y):
        """Performs multiplication in a separate process with input validation."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            print(f"Process {current_process().name}: Result = {x * y}")
        except ValueError:
            print("Error: Invalid input! Please enter numeric values.")

def register(handler):
    """Registers the MultiplyCommand dynamically."""
    handler.register_command("multiply", MultiplyCommand())