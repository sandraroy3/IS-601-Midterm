# Class for modules and namespace 

from app.commands import CommandHandler
from app.commands.discord import DiscordCommand
from app.commands.exit._init__ import ExitCommand
from app.commands.goodbye._init__ import GoodByeCommand
from app.commands.greet._init__ import GreetCommand
from app.commands.menu._init__ import MenuCommand
from app.operations import add, subtract, multiply, divide

class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodByeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())

        print("Type 'exit' to exit.")
        while True: # REPL: Read Evaluate Print Loop
            self.command_handler.execute_command(input(">>").strip())
