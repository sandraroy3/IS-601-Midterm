from app.commands import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")

def register(handler):
    handler.register_command("greet", GreetCommand())