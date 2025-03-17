from app.commands import Command
from multiprocessing import current_process

class MultiplyCommand(Command):
    """Command that performs multiplication with error handling."""

    def execute(self, x, y):
        """Performs multiplication in a separate process."""
        try:
            print(f"Process {current_process().name}: Result = {x * y}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

def register(handler):
    """Registers the MultiplyCommand dynamically."""
    handler.register_command("multiply", MultiplyCommand())
