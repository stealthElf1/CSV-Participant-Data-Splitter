# CSV Alias Splitter

Splits a CSV file into multiple output files, one file per unique value in the `alias` column.

## Prerequisites

```
pip install pandas
```

## Setup

Customize the three variables at the beginning of `split_by_alias_simple.py`:

```python
INPUT_FILE = r“Input_path/file.csv” 
SEPERATOR = “,”                        
OUTPUT_FOLDER = r“Output_path”         
```

## Running the Script

```
python split_by_alias_simple.py
```

## What the script does

1. Reads `INPUT_FILE`.
2. Removes completely empty rows.
3. Groups the rows by the `alias` column.
4. Writes a separate CSV file for each alias to `OUTPUT_FOLDER`, each including a header row

## Note

If the error `KeyError: ‘alias’` occurs, `SEPERATOR` does not match the actual delimiter in the file (e.g., a comma instead of a tab). Check the raw file in a text editor to find the correct character.
