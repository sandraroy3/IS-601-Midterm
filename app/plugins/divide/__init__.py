import logging
from app.commands import Command
from multiprocessing import current_process

# Set up the logger
logger = logging.getLogger('calc_logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File handler to log to a file
file_handler = logging.FileHandler('calc_history.log')
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

class DivideCommand(Command):
    """Command that performs division with error handling for invalid inputs."""

    def execute(self, x, y):
        """Performs division while handling division by zero and invalid inputs."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            if y == 0:
                error_msg = "Error: Division by zero is not allowed."
                logger.error(f"Process {current_process().name}: {error_msg}")
                print(error_msg)
                return error_msg

            result = x / y
            # Log the result with process information
            logger.info(f"Process {current_process().name}: Command 'divide' executed with result = {result}")
            print(f"Process {current_process().name}: Result = {result}")
            return result

        except ValueError:
            error_msg = "Invalid input! Please enter numeric values."
            logger.error(f"Process {current_process().name}: {error_msg}")
            print(error_msg)
            return error_msg
        except ZeroDivisionError as e:
            # Log division by zero error
            logger.error(f"Process {current_process().name}: {str(e)}")
            print(str(e))
            return str(e)

def register(handler):
    """Registers the DivideCommand dynamically with CommandHandler."""
    handler.register_command("divide", DivideCommand())
