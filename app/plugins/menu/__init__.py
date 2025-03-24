from app.commands import Command

class MenuCommand(Command):
    """Displays all available commands dynamically when executed, excluding itself."""

    def __init__(self, handler):
        self.handler = handler  # Store reference to CommandHandler

    def execute(self):
        """Prints all registered commands with descriptions."""
        menu = [
            "\n=== Calculator App Menu ===",
            "Available commands:",
            "  - add <x> <y>      : Add two numbers",
            "  - subtract <x> <y>  : Subtract y from x",
            "  - multiply <x> <y>  : Multiply two numbers",
            "  - divide <x> <y>    : Divide x by y",
            "  - greet            : Display a greeting",
            "\nUtility commands:",
            "  - menu             : Show this menu again",
            "  - clear_history    : Clear command history",
            "  - delete_history <index> : Delete a specific history entry",
            "  - exit            : Exit the application",
            "\nType your command at the prompt below:"
        ]
        menu_text = "\n".join(menu)
        print(menu_text)
        return menu_text

def register(handler):
    """Registers the MenuCommand dynamically."""
    handler.register_command("menu", MenuCommand(handler))