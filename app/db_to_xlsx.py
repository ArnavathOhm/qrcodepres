from .models import get_db_columns, get_db_items
import xlsxwriter


def create_db_xlsx(filename="Presence.xlsx"):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    data_columns = get_db_columns()
    data_items = get_db_items()
    data_lists = [list(data.values()) for data in data_items]

    # row and column index
    row = 0
    col = 0

    # write data to worksheet
    bold = workbook.add_format({"bold": True})
    for i in range(len(data_columns)):
        worksheet.write(row, col + i, data_columns[i], bold)
    row += 1
    for vals in data_lists:
        for i in range(len(data_columns)):
            worksheet.write(row, col + i, vals[i])
        row += 1

    workbook.close()
