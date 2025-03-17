import os
import pkgutil
import logging
import logging.config
import importlib
import pandas as pd
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):  # Constructor
        os.makedirs('logs', exist_ok=True)
        os.makedirs('history', exist_ok=True)  # Ensure the history folder exists
        self.configure_logging()
        logging.info("Logger successfully configured.")

        load_dotenv()
        logging.info("Environment variables loaded.")

        self.command_handler = CommandHandler()
        logging.info("Command handler initialized.")

        # Initialize an empty DataFrame for command history
        self.command_history = pd.DataFrame(columns=["Command", "Result", "Timestamp"])

        # Load previous history if available
        self.load_history()

    def configure_logging(self):
        """Configure logging with file and console handlers."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler("logs/app.log"),  # Logs to file
                    logging.StreamHandler()  # Logs to console
                ]
            )
        logging.info("Logging configured.")

    def load_history(self):
        """Load command history from the CSV file."""
        history_path = 'history/command_history.csv'
        if os.path.exists(history_path):
            self.command_history = pd.read_csv(history_path)
            logging.info(f"Loaded command history from {history_path}.")
        else:
            logging.info("No previous command history found.")

    def save_command_history(self):
        """Save the command history to a CSV file."""
        history_path = 'history/command_history.csv'
        self.command_history.to_csv(history_path, index=False)
        logging.info(f"Command history saved to {history_path}.")

    def clear_history(self):
        """Clear the command history."""
        self.command_history = pd.DataFrame(columns=["Command", "Result", "Timestamp"])
        self.save_command_history()
        logging.info("Command history cleared.")

    def delete_history_record(self, command_index):
        """Delete a specific history record by index."""
        if 0 <= command_index < len(self.command_history):
            self.command_history = self.command_history.drop(index=command_index)
            self.command_history = self.command_history.reset_index(drop=True)
            self.save_command_history()
            logging.info(f"Deleted command at index {command_index}.")
        else:
            logging.error(f"Invalid command index: {command_index}.")

    def load_plugins(self):
        """Dynamically load all plugins in the 'app.plugins' directory."""
        plugins_package = 'app.plugins'
        try:
            package_path = importlib.import_module(plugins_package).__path__
        except ModuleNotFoundError:
            logging.warning(f"Plugins package '{plugins_package}' not found.")
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules(package_path):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Registers plugin commands dynamically."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                command_name = getattr(item, "name", plugin_name)  # Allow explicit command names
                try:
                    if command_name.lower() == "menu":  
                        # Only pass handler if required (for MenuCommand)
                        self.command_handler.register_command(command_name, item(self.command_handler))
                    else:
                        # Instantiate normally for all other commands
                        self.command_handler.register_command(command_name, item())

                    logging.info(f"Command '{command_name}' from plugin '{plugin_name}' registered.")
                except TypeError as e:
                    logging.error(f"Error instantiating command '{command_name}': {e}")

    def start(self):
        """Starts the calculator application with a REPL loop."""
        self.load_plugins()
        logging.info("App started. Type 'exit' to exit, 'clear_history' to clear, or 'delete_history <index>' to delete a record.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("App exited.")
                    break
                elif cmd_input.lower() == 'clear_history':
                    self.clear_history()
                elif cmd_input.lower().startswith('delete_history'):
                    try:
                        _, command_index = cmd_input.split()
                        self.delete_history_record(int(command_index))
                    except ValueError:
                        logging.error("Please provide a valid index to delete.")
                else:
                    try:
                        # Execute the command and capture the result
                        result = self.command_handler.execute_command(cmd_input)

                        # If the result is None, set it to 'No result'
                        if result is None:
                            result = 'No result'

                        # Save command and result to history
                        timestamp = pd.to_datetime('now')
                        new_history = pd.DataFrame([{
                            "Command": cmd_input,
                            "Result": result,
                            "Timestamp": timestamp
                        }])

                        # Concatenate the new history entry to the existing history
                        self.command_history = pd.concat([self.command_history, new_history], ignore_index=True)

                        # Save the history to CSV after each command execution
                        self.save_command_history()

                    except KeyError:
                        logging.error(f"Unknown command: {cmd_input}. Try again.")
        except KeyboardInterrupt:
            logging.info("App interrupted and exiting gracefully.")
        finally:
            logging.info("App shutdown.")

if __name__ == "__main__":
    app = App()
    app.start()
