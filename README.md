# README

This code generates a string of SQL statements that represent dates from '01/01/2023' to the current date.

## Prerequisites

To run this code, you need:

- Python 3.7 or higher

## Usage

1. Open a Python environment or editor of your choice.
2. Copy and paste the code into a Python script file (e.g., `generate_dates.py`).
3. Run the script using a Python interpreter:
   ```shell
   python generate_dates.py

   E.g. '.....................
        ......................
        SELECT '2023-06-06'::date AS date_month
        UNION ALL
        SELECT '2023-06-07'::date AS date_month
        UNION ALL
        SELECT '2023-06-08'::date AS date_month
        UNION ALL
        ......................
        ......................'


The script will generate a string of SQL statements representing dates from '01/01/2023' to the current date.
The resulting SQL statements will be printed to the console.