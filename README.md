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

### Quick start (Python)

1. Install dependencies:

```bash
pip install -e .
```

2. Start the app in GUI mode:

```bash
python main.py
```

3. In the app dialogs:
- Select your SQLite database (`.db`, `.sqlite`, `.sqlite3`)
- Choose where to save the Excel file (`.xlsx`)

### Command line usage

Convert using command line (no dialogs):

```bash
python main.py path/to/database.db
```

Convert and choose output path:

```bash
python main.py path/to/database.db -o output.xlsx
```

Force GUI explicitly:

```bash
python main.py --gui
```

### Example

```bash
python main.py example/trades.db -o example/trades.xlsx
```

### Use without Python (Windows .exe)

After building, run:

`dist/DatabaseConverter.exe`

The `.exe` opens the same file picker workflow and creates the Excel file you choose.

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

## Build Native Windows Executable (.exe)

Install PyInstaller once:

```bash
pip install pyinstaller
```

Build executable:

```powershell
./build_exe.ps1
```

Output file:

`dist/DatabaseConverter.exe`

You can run that `.exe` directly on Windows to use the file picker interface.

Customize app identity:

- Icon file: `assets/DatabaseConverter.ico`
- Version metadata: `version_info.txt`

Edit `version_info.txt` to change product name, company, and version shown in Windows file properties.

## Build Release ZIP

Create a distributable versioned ZIP (builds EXE first, then zips it):

```powershell
./build_release.ps1
```

Output example:

`dist/DatabaseConverter-v1.0.0.0-win64.zip`

The ZIP version is read from `ProductVersion` in `version_info.txt`.

## License

MIT
