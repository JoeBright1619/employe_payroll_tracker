import os

def clear_screen():
    # Windows = cls, Linux/Mac = clear
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")
