import os

def clear_screen():
    """Clear the terminal window (cls for Windows, clear elsewhere)."""
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Block until the user explicitly continues execution."""
    input("\nPress Enter to continue...")
