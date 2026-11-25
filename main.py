#!/usr/bin/env python3
"""Look up a birthday by first and last name."""

import argparse

from bdpackage.bdmodule import get_birthdays, return_birthday


def main():
    """Parse a name and print its birthday when available."""
    birthdays = get_birthdays()
    firstnames = list(
        dict.fromkeys(name.split(" ", 1)[0] for name in birthdays)
    )
    lastnames = list(
        dict.fromkeys(name.split(" ", 1)[1] for name in birthdays)
    )

    parser = argparse.ArgumentParser(
        description="Find the birthday of a person."
    )
    parser.add_argument(
        "--firstname",
        required=True,
        choices=firstnames,
        help="Provide the first name (e.g., --firstname Albert)",
    )
    parser.add_argument(
        "--lastname",
        required=True,
        choices=lastnames,
        help="Provide the last name (e.g., --lastname Einstein)",
    )

    args = parser.parse_args()
    return_birthday(f"{args.firstname} {args.lastname}")


if __name__ == "__main__":
    main()
