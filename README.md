# Birthday lookup

Look up a person's birthday using the data in `birthdays.csv`. The CSV has two columns: `Name` and `Birthday`.

Run the program with both required options:

```bash
python3 main.py --firstname Albert --lastname Einstein
```

Expected output:

```text
Albert Einstein's birthday is 03/14/1879.
```

Use `python3 main.py --help` to see the available first and last names. The names are read from the CSV when the program runs. Each option is checked separately, so a valid but unmatched combination such as `Albert Franklin` produces the “Sadly, ...” message.

`bdpackage/write_dict.py` contains the original hard-coded dictionary and was run once to create `birthdays.csv`. The lookup code reads the CSV; it does not import the dictionary from that script. To change the available birthdays, edit `birthdays.csv`.

## Credits

The original birthday example comes from [Practice Python](https://www.practicepython.org/) by Michele Pratusevich and is released under [CC BY](https://www.practicepython.org/about/).
