"""Create birthdays.csv from the original birthday dictionary once."""

import csv
from pathlib import Path


BIRTHDAYS = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815",
    "Donald Trump": "06/14/1946",
    "Rowan Atkinson": "01/6/1955",
}

CSV_PATH = Path(__file__).resolve().parent.parent / "birthdays.csv"


def main():
    """Write the original birthday data with Name and Birthday columns."""
    with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["Name", "Birthday"], lineterminator="\n"
        )
        writer.writeheader()
        for name, birthday in BIRTHDAYS.items():
            writer.writerow({"Name": name, "Birthday": birthday})


if __name__ == "__main__":
    main()
