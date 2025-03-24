"""App initialization and core functionality."""
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
            try:
                self.command_history = pd.read_csv(history_path)
                logging.info(f"Loaded command history from {history_path}.")
            except pd.errors.EmptyDataError:
                self.command_history = pd.DataFrame(columns=["Command", "Result", "Timestamp"])
                logging.info("Created new command history DataFrame.")
        else:
            logging.info("No previous command history found.")

    def save_command_history(self):
        """Save the command history to a CSV file."""
        history_path = 'history/command_history.csv'
        try:
            self.command_history.to_csv(history_path, index=False)
            logging.info(f"Command history saved to {history_path}.")
        except Exception as e:
            logging.error(f"Error saving command history: {str(e)}")

    def clear_history(self):
        """Clear the command history."""
        try:
            self.command_history = pd.DataFrame(columns=["Command", "Result", "Timestamp"])
            self.save_command_history()
            logging.info("Command history cleared.")
            return "Command history cleared successfully."
        except Exception as e:
            error_msg = f"Error clearing history: {str(e)}"
            logging.error(error_msg)
            return error_msg

    def delete_history_record(self, command_index):
        """Delete a specific history record by index."""
        try:
            command_index = int(command_index)  # Ensure index is an integer
            if 0 <= command_index < len(self.command_history):
                # Get the command being deleted for logging
                deleted_command = self.command_history.iloc[command_index]["Command"]
                
                # Drop the row and reset index
                self.command_history = self.command_history.drop(self.command_history.index[command_index])
                self.command_history = self.command_history.reset_index(drop=True)
                
                # Save changes
                self.save_command_history()
                
                msg = f"Deleted command '{deleted_command}' at index {command_index}"
                logging.info(msg)
                return msg
            else:
                error_msg = f"Invalid command index: {command_index}. Index must be between 0 and {len(self.command_history)-1}"
                logging.error(error_msg)
                return error_msg
        except ValueError:
            error_msg = f"Invalid index format: {command_index}. Must be an integer."
            logging.error(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Error deleting history record: {str(e)}"
            logging.error(error_msg)
            return error_msg

    def execute_command(self, cmd_input):
        """Execute a command and update history."""
        if not cmd_input.strip():
            return "Please enter a command"

        cmd_input = cmd_input.strip()
        
        # Handle special history commands directly
        if cmd_input == "clear_history":
            return self.clear_history()
        
        if cmd_input == "delete_history":
            return "Error: delete_history requires an index argument"
            
        if cmd_input.startswith("delete_history "):
            try:
                index = cmd_input.split()[1]
                return self.delete_history_record(index)
            except IndexError:
                return "Error: delete_history requires an index argument"
        
        # Handle regular commands
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
