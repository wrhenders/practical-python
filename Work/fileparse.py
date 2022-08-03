# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        # If a column selector was given, find the indicies of specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indicies = [headers.index(colname) for colname in select]
            headers = select
        else:
            indicies = []
        records = []
        for i, row in enumerate(rows):
            if not row:  # Skip rows with no data
                continue
            # Filter the row is specific columns were selected
            if indicies:
                row = [row[index] for index in indicies]

            # Add types if specified
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {i}: Couldn't convert {row}")
                        print(f"Row {i}: Reason {e}")
                    continue

            # Make dictionary or touple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records
