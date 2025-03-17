from app.commands import Command

class ExitCommand(Command): # inherits from Command
    def execute(self):
        print("Exiting...!")