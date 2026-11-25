"""Read birthday data from CSV and look up people by name."""

import csv
from pathlib import Path


CSV_PATH = Path(__file__).resolve().parent.parent / "birthdays.csv"


def get_birthdays():
    """Map full names to birthdays using the CSV file."""
    with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return {row["Name"]: row["Birthday"] for row in reader}


def print_birthdays():
    """Print the names whose birthdays are available."""
    print(
        "Welcome to the birthday dictionary. "
        "We know the birthdays of these people:"
    )
    for name in get_birthdays():
        print(name)


def return_birthday(name):
    """Print the birthday of a person, or say when it is unknown."""
    birthdays = get_birthdays()
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}.")
    else:
        print(f"Sadly, we don't have {name}'s birthday.")
