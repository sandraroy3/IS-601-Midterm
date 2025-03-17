from app.commands import Command
from multiprocessing import current_process

class DivideCommand(Command):
    """Command that performs division with error handling for invalid inputs."""

    def execute(self, x, y):
        """Performs division while handling division by zero and invalid inputs."""
        try:
            x = int(x)  # Convert input to integer
            y = int(y)  # Convert input to integer
            if y == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")

            print(f"Process {current_process().name}: Result = {x / y}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except ZeroDivisionError as e:
            print(e)  # Displays custom division by zero error message

def register(handler):
    """Registers the DivideCommand dynamically with CommandHandler."""
    handler.register_command("divide", DivideCommand())