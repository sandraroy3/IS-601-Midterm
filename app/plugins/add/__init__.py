from app.commands import Command
from multiprocessing import current_process
import logging

logger = logging.getLogger(__name__)

class AddCommand(Command):
    """Command to add two numbers."""
    
    def execute(self, x, y):
        """Perform addition."""
        try:
            x = int(x)
            y = int(y)
            result = x + y
            logger.info(f"Add command executed: {x} + {y} = {result}")
            return result
        except ValueError as e:
            logger.error(f"Invalid input for add command: {e}")
            return "Invalid input"


def register(handler):
    """Registers the AddCommand dynamically."""
    handler.register_command("add", AddCommand())