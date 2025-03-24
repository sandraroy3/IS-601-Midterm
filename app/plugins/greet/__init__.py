import logging
from app.commands import Command
from multiprocessing import current_process

class GreetCommand(Command):
    """A simple command that prints a greeting message."""

    def execute(self):
        """Prints a greeting message and the process name."""
        message = f"Process {current_process().name}: Hello, World!"
        logging.info(message)
        print(message)
        return message

def register(handler):
    """Registers the GreetCommand dynamically with CommandHandler."""
    handler.register_command("greet", GreetCommand())