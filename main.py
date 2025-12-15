filepath = input("Enter your word path: ")

from core.parser import Parser
from ui.cli import CLI

CLI(Parser(filepath))