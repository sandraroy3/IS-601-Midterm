from app.commands import Command

class GoodByeCommand(Command):
    def execute(self):
        print("Goodbye")