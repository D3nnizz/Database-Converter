# Database Converter

Convert SQLite databases to Excel files with one sheet per table. Perfect for importing into Google Sheets, LibreOffice Calc, or Microsoft Excel.

## Features

- Reads SQLite database files
- Creates Excel (.xlsx) file with one sheet per table
- Automatically includes column headers
- Handles multiple tables efficiently
- Works offline, no API setup required

## Setup

Install dependencies:

```bash
pip install -e .
```

Or using uv:

```bash
uv pip install -e .
```

## Usage

### Windows GUI (simple file picker)

Run without arguments to open a file dialog:

```bash
python main.py
```

Or force GUI mode explicitly:

```bash
python main.py --gui
```

The app will:
1. Ask you to select a SQLite database file
2. Ask where to save the converted Excel file

Basic usage:

```bash
python main.py path/to/database.db
```

Specify custom output file:

```bash
python main.py path/to/database.db -o output.xlsx
```

### Example

Convert the example database:

```bash
python main.py example/trades.db
```

This creates `trades.xlsx` with one sheet per table.

## Using with Google Sheets

1. Run the converter to create an Excel file
2. Go to [Google Drive](https://drive.google.com)
3. Upload the .xlsx file
4. Double-click to open with Google Sheets
5. (Optional) Click File > Save as Google Sheets to convert it

## Using with LibreOffice

Just open the .xlsx file directly in LibreOffice Calc.

## Advanced: Direct Google Sheets Upload

If you prefer to upload directly to Google Sheets via API (more complex, requires setup), see `google_sheets_direct.py` and set up Google Cloud credentials. **Note:** This method can have quota issues with service accounts.

## Requirements

- Python >= 3.13
- SQLite database file

## License

MIT
