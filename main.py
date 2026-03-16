import sqlite3
import argparse
from pathlib import Path
from openpyxl import Workbook
import tkinter as tk
from tkinter import filedialog, messagebox


def sqlite_to_excel(db_path, output_file=None):
    """
    Convert SQLite database to Excel file with one sheet per table.
    
    Args:
        db_path: Path to SQLite database file
        output_file: Output Excel file path (defaults to database name.xlsx)
    """
    # Set default output file name
    if output_file is None:
        output_file = f"{Path(db_path).stem}.xlsx"
    
    # Connect to SQLite database
    print(f"Reading database: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [row[0] for row in cursor.fetchall()]
    
    if not tables:
        print("No tables found in database!")
        conn.close()
        return
    
    print(f"Found {len(tables)} table(s): {', '.join(tables)}")
    
    # Create Excel workbook
    wb = Workbook()
    wb.remove(wb.active)  # Remove default sheet
    
    # Process each table
    for table_name in tables:
        print(f"Processing table: {table_name}")
        
        # Get table data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        column_names = [description[0] for description in cursor.description]
        
        # Create worksheet
        ws = wb.create_sheet(title=table_name)
        
        # Write headers
        ws.append(column_names)
        
        # Write data rows
        for row in rows:
            ws.append(list(row))
        
        print(f"  ✓ Added {len(rows)} rows to sheet '{table_name}'")
    
    # Save workbook
    wb.save(output_file)
    conn.close()
    
    print("\n✓ Export complete!")
    print(f"Excel file created: {output_file}")
    print("\nTo use in Google Sheets:")
    print("1. Go to https://drive.google.com")
    print(f"2. Upload this file: {output_file}")
    print("3. Double-click to open with Google Sheets")


def run_gui():
    """Run a minimal Windows-friendly GUI for database conversion."""
    root = tk.Tk()
    root.withdraw()

    db_path = filedialog.askopenfilename(
        title="Select SQLite Database",
        filetypes=[
            ("SQLite databases", "*.db *.sqlite *.sqlite3"),
            ("All files", "*.*"),
        ],
    )

    if not db_path:
        return

    default_name = f"{Path(db_path).stem}.xlsx"
    output_file = filedialog.asksaveasfilename(
        title="Save Excel File As",
        defaultextension=".xlsx",
        initialfile=default_name,
        filetypes=[("Excel Workbook", "*.xlsx")],
    )

    if not output_file:
        return

    try:
        sqlite_to_excel(db_path, output_file)
        messagebox.showinfo(
            title="Conversion Complete",
            message=f"Excel file created:\n{output_file}",
        )
    except Exception as exc:
        messagebox.showerror(
            title="Conversion Failed",
            message=f"An error occurred while converting the database:\n{exc}",
        )


def main():
    parser = argparse.ArgumentParser(
        description='Convert SQLite database to Excel file with one sheet per table.'
    )
    parser.add_argument(
        'database',
        nargs='?',
        type=str,
        help='Path to SQLite database file (omit to open GUI)'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Output Excel file path (default: database_name.xlsx)'
    )
    parser.add_argument(
        '--gui',
        action='store_true',
        help='Open the file picker GUI'
    )
    
    args = parser.parse_args()
    
    if args.gui or not args.database:
        run_gui()
        return

    # Validate database file exists
    if not Path(args.database).exists():
        print(f"Error: Database file not found: {args.database}")
        return
    
    try:
        sqlite_to_excel(args.database, args.output)
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()
