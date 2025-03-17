from venv import logger
from app.commands import Command
from multiprocessing import current_process

class MultiplyCommand(Command):
    """Command that performs multiplication with error handling."""

    def execute(self, x, y):
        """Performs multiplication in a separate process with input validation."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            result = x * y
            # Log the result with process information
            logger.info(f"Process {current_process().name}: Command 'add' executed with result = {result}")
            print(f"Process {current_process().name}: Result = {result}")  # Optionally print to the console
            return result
        except ValueError:
            logger.error(f"Process {current_process().name}: Invalid input! Please enter numeric values.")
            print("Invalid input! Please enter numeric values.")

def register(handler):
    """Registers the MultiplyCommand dynamically."""
    handler.register_command("multiply", MultiplyCommand())