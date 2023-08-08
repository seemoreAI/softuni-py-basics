from openpyxl import Workbook
workbook = Workbook()
current_sheet = workbook.active
current_sheet["A1"] = '1'

workbook.save(filename='example.xlsx')



