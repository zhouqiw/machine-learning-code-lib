# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: demo_update.py
@time: 2017/4/12 上午3:03
"""
import  MySQLdb

def func():



    # 创建插入SQL语句
    query = "update orders  set name = VALUES (%s)"

    values= 'ups_demo'



def selecl_all(object):
    # 建立一个MySQL连接
    conn = MySQLdb.connect(host="localhost", user="root", passwd="rooter" )

    # 获得游标对象, 用于逐行遍历数据库数据
    cur = conn.cursor()

    conn.select_db("imooc")

    # cur.execute('insert into orders()')
    # cur.execute("insert into orders(id, name, AddrId, MgrobjTypeID, AgentBM') values('777','dename','0755','80808080','89080')")

    sql = "insert into  yum(id,name,addrss,phone_number,work) VALUES (%s, %s, %s, %s, %s)"


    cur.execute(sql, object)

    # 关闭游标
    cur.close()

    # 提交
    conn.commit()

    # 关闭数据库连接
    conn.close()

    print 'ok'






if __name__ == '__main__':

    value1 = (23, 'zhouqir', 'shenzhen', '18903052976', 'devlopment');

    selecl_all(value1)