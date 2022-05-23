from clint.textui import colored
from colorama import Fore, Back, Style
from pyfiglet import Figlet

def vitac(text):
    result = Figlet()
    return colored.red(result.renderText(text))

def plnic(text):
    result = Figlet()
    return colored.blue(result.renderText(text))

def konvert(text):
    result = Figlet()
    return colored.red(result.renderText(text))

def mainmenu(text):
    result = Figlet()
    return colored.yellow(result.renderText(text))