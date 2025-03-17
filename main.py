import importlib
import os
from app.commands import CommandHandler

# Initialize the CommandHandler to manage all commands
handler = CommandHandler()

def load_plugins():
    """Dynamically loads all plugins (commands) from the plugins directory."""
    package_name = "app.plugins"
    plugins_dir = package_name.replace(".", "/")  # Converts package name to directory path

    for subdir in os.listdir(plugins_dir):
        subdir_path = os.path.join(plugins_dir, subdir)
        if os.path.isdir(subdir_path):  # Ensure it's a directory
            module_name = f"{package_name}.{subdir}"  # Construct module path
            try:
                module = importlib.import_module(module_name)  # Import module dynamically
                if hasattr(module, "register"):
                    module.register(handler)  # Register command dynamically
            except Exception as e:
                print(f"Failed to load plugin {module_name}: {e}")  # Handle import errors

# Load all commands from the plugins directory
load_plugins()

def repl():
    """
    Implements the Read-Evaluate-Print-Loop (REPL) to interact with users.
    Now, inputs are collected in the main process before being passed to commands.
    """
    print("Welcome to the Interactive Calculator! Type 'menu' for commands or 'exit' to quit.")

    while True:
        user_input = input("Enter command: ").strip().lower()

        if user_input == "exit":
            print("Exiting program...")
            break
        elif user_input == "menu":
            print("Available commands:", ", ".join(handler.commands.keys()))
        elif user_input in handler.commands:
            try:
                # Ask for numbers only if the command requires arguments
                if user_input in ["add", "subtract", "multiply", "divide"]:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    handler.execute_command(user_input, x, y)  # Pass inputs to process
                else:
                    handler.execute_command(user_input)  # No arguments for commands like 'greet' or 'menu'
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Unknown command. Type 'menu' to see available commands.")


if __name__ == "__main__":
    repl()  # Start the REPL loop when script runs
