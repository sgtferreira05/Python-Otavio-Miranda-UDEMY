# openpyxl - Reading and Writing Excel Files in Python
# xlsx - Excel Workbook
# xlsm - Excel Macro-Enabled Workbook
# xltx - Excel Template Workbook
# xltm - Excel Macro-Enabled Template Workbook

# With openpyxl, we can create and manipulate Excel files in Python.
# It allows us to read, write, and modify Excel files in the xlsx and xlsm formats.
# Its usefull to create reports, data analysis, and automate tasks in Excel.
# It is a powerful library that provides a lot of functionality for working with Excel files.

from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell

from openpyxl.worksheet.worksheet import Worksheet

root_folder = Path(__file__).parent
workbook_path = root_folder / 'workbook.xlsx'

# Loading a excel file
workbook:Workbook = load_workbook(workbook_path)  # Create a new workbook
# worksheet: Worksheet = workbook.active  # Get the active worksheet

# Name to the spreadsheet
sheet_name = 'Students'
# Get the worksheet by name
worksheet: Worksheet = workbook[sheet_name]

row: tuple[Cell]
for row in worksheet.iter_rows(min_row=2, max_row=worksheet.max_row, min_col=1, max_col=3):
    for cell in row:
        print(cell.value, end='\t')

        if cell.value == 'Maria':
            worksheet.cell(cell.row, 2, 23)
    print()

# worksheet['B3'].value = 20  # Update the value of cell B3
# worksheet['C3'].value = 10.0  # Update the value of cell C3

workbook.save(workbook_path)  # Save the workbook to a file
