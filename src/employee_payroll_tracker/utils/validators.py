def validate_float(prompt: str) -> float:
    """
    Ask repeatedly until the user enters a valid float.
    """
    while True:
        value = input(prompt).strip()

        try:
            return float(value)
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def validate_positive_int(prompt: str) -> int:
    """
    Ask until the user enters a valid positive integer.
    """
    while True:
        value = input(prompt).strip()

        if value.isdigit() and int(value) > 0:
            return int(value)

        print("Please enter a positive whole number.")
