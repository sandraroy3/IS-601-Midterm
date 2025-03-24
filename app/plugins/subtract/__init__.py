from venv import logger
from app.commands import Command
from multiprocessing import current_process

class SubtractCommand(Command):
    """Command that performs subtraction with error handling."""

    def execute(self, x, y):
        """Performs subtraction in a separate process."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            result = x - y
            # Log the result with process information
            logger.info(f"Process {current_process().name}: Command 'subtract' executed with result = {result}")
            print(f"Process {current_process().name}: Result = {result}")
            return result
        except ValueError:
            error_msg = "Invalid input! Please enter numeric values."
            logger.error(f"Process {current_process().name}: {error_msg}")
            print(error_msg)
            return error_msg

def register(handler):
    """Registers the SubtractCommand dynamically."""
    handler.register_command("subtract", SubtractCommand())