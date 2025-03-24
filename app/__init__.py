import os
import pkgutil
import logging
import logging.config
import importlib
import pandas as pd
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command
from datetime import datetime

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

        # Initialize an empty DataFrame with proper columns
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

    def execute_command(self, cmd_input):
        """Execute a command and update history."""
        result = self.command_handler.execute_command(cmd_input)
        
        # Add command to history
        new_entry = pd.DataFrame({
            "Command": [cmd_input],
            "Result": [str(result)],
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        })
        
        self.command_history = pd.concat([self.command_history, new_entry], ignore_index=True)
        self.save_command_history()
        return result

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
        """Register commands from a plugin module."""
        if hasattr(plugin_module, 'register'):
            try:
                plugin_module.register(self.command_handler)
                logging.info(f"Successfully registered commands from plugin {plugin_name}")
            except Exception as e:
                logging.error(f"Error registering commands from plugin {plugin_name}: {e}")
        else:
            logging.warning(f"Plugin {plugin_name} has no register function")

    def start(self):
        """Start the calculator application."""
        self.load_plugins()
        
        # Display welcome message and menu
        self.command_handler.execute_command("menu")
        
        while True:
            try:
                command = input("\nEnter command: ").strip()
                if command.lower() == "exit":
                    print("Goodbye!")
                    break
                    
                self.execute_command(command)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = App()
    app.start()
