import logging
from app.commands import Command
from multiprocessing import current_process

class GreetCommand(Command):
    """A simple command that prints a greeting message."""

    def execute(self):
        logging.info("Hello world!")
        """Prints a greeting message and the process name."""
        print(f"Process {current_process().name}: Hello, World!")

def register(handler):
    """Registers the GreetCommand dynamically with CommandHandler."""
    handler.register_command("greet", GreetCommand())