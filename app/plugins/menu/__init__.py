from app.commands import Command

class MenuCommand(Command):
    """Displays all available commands dynamically when executed, excluding itself."""

    def __init__(self, handler):
        self.handler = handler  # Store reference to CommandHandler

    def execute(self):
        """Prints all registered commands, but hides 'menu' from the list."""
        commands_list = sorted([cmd for cmd in self.handler.commands.keys() if cmd != "menu"])
        print("Available commands:", ", ".join(commands_list))

def register(handler):
    """Registers the MenuCommand dynamically."""
    handler.register_command("menu", MenuCommand(handler))