# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo_1.py
@time: 2017/4/14 上午9:04
"""


def func():
    import xlrd
    import MySQLdb
    # Open the workbook and define the worksheet
    book = xlrd.open_workbook("/Users/zhouqi/Desktop/qd.xlsx")
    sheet = book.sheet_by_name("MgrObj")

    # 建立一个MySQL连接
    database = MySQLdb.connect(host="localhost", user="root", passwd="rooter", db="imooc",charset="utf8")

    # 获得游标对象, 用于逐行遍历数据库数据
    cursor = database.cursor()

    # 创建插入SQL语句
    query = "INSERT INTO orders (Id, name, AddrId, MgrobjTypeId, AgentBM) VALUES (%s, %s, %s, %s, %s)"

    # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
    for r in range(2, sheet.nrows):

        Id = sheet.cell(r, 0).value
        name = sheet.cell(r, 1).value
        AddrId = sheet.cell(r, 2).value
        MgrobjTypeId= sheet.cell(r, 3).value
        AgentBM = sheet.cell(r, 4).value


        values = (Id, name, AddrId, MgrobjTypeId, AgentBM)

        # 执行sql语句
        cursor.execute(query, values)

    # 关闭游标
    cursor.close()

    # 提交
    database.commit()

    # 关闭数据库连接
    database.close()

    # 打印结果
    print ""
    print "Done! "
    print ""





class Main(object):
    def __init__(self):
        func()


if __name__ == '__main__':
    Main()
