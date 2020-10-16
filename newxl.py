import xlsxwriter
import sqlite3

conn = sqlite3.connect('customer.db', check_same_thread=False)
cu = conn.cursor()
cu.execute("SELECT * FROM student")
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('stud.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = cu.fetchall()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for Sno,Name,Experience in (expenses):
    worksheet.write(row, col,     Sno)
    worksheet.write(row, col + 1, Name)
    worksheet.write(row, col + 2, Experience)
    row += 1

# Write a total using a formula.
# worksheet.write(row, 0, 'Total')
# worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()