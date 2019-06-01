#coding=utf-8
import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    workbook = xlrd.open_workbook(ur'/home/work/code/python_learn/data/vid.xlsx')
    sheet_names = workbook.sheet_names()
    for sheetname in sheet_names:
        print sheetname
    sheet2_name = workbook.sheet_names()[1]

    #根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(2) # sheet 索引从0开始
   # sheet2 = workbook.sheet_by_name(u'5.14号-166')

    # sheet的名称,行数,列数
    name = sheet2.name
    nrows = sheet2.nrows
    ncols = sheet2.ncols
    print name
    print ncols
    print nrows

    # 获取整行和整列的值(数组)
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(0) # 获取第一列内容
    
#    for row in rows:
#        print rows
#    for col in cols:
#        print col
#
    for i in range(nrows):
        row = ''
        for j in range(ncols):
            row = row + sheet2.row(i)[j].value.encode('utf-8') + ","
        print row[:-1]

    #获取单元格内容
    print sheet2.cell(1, 0).value.encode('utf-8')
    print sheet2.cell_value(1, 0).encode('utf-8')
    print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    print sheet2.cell(1, 0).ctype

if __name__ == '__main__':
    read_excel()
