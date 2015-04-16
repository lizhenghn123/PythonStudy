#!/usr/bin/env python
# coding=utf-8
#author = lizheng
#date = 2015-04-16
import os
import time
import random
import MySQLdb as db
# should install MySQL-python
# on Linux(centos) : yum install MySQL-python
# on windows       : http://www.codegood.com/downloads 

dbhost = "192.168.14.215"
dnname = "mrcp1"
dbuser = "root"
dbpass = "123456"
dbtable = "tb"

def getConnection():
    pass

def test_mysqldb1():
    cxn = db.connect(host=dbhost, user=dbuser, passwd=dbpass)
    cxn.query("DROP DATABASE %s" % dnname)
    cxn.query("CREATE DATABASE %s" % dnname)
    cxn.select_db(dnname)
    cxn.commit()
    
def test_mysqldb2():
    cxn = db.connect(host=dbhost, db=dnname, user=dbuser, passwd=dbpass)

    cxn.query("DROP TABLE IF EXISTS %s" % dbtable)
    cxn.query("CREATE TABLE %s(id int(20) NOT NULL, name char(20), UNIQUE KEY(id), PRIMARY KEY(id))" % dbtable)
    cxn.commit()

    cur = cxn.cursor()
    # add
    cur.execute("insert into tb VALUES('1', 'lizheng')")
    cur.execute("insert into tb VALUES(2, 'wangjiu')")
    # select
    cur.execute("select * from %s" % dbtable)
    # update
    cur.execute("update %s set name='zxcvbn' where id = 2" % dbtable)
    # delete
    cur.execute("delete from %s where id = 2" % dbtable);
    
    #print("insert into tb VALUES('%s', '%s')", [(k,v) for k,v in tb_data.items()])
    cur.execute("insert into tb VALUES('%s', '%s')" % (23, 'zxcv'))

    tb_data = {123:'n123', 345:'v345', 456:'f456'}
    cur.executemany("insert into tb VALUES(%s, %s)" , [(45, '555555')])
    cur.executemany("insert into tb VALUES(%s, %s)" , [(k,v) for k,v in tb_data.items()])
    
    cur.execute("select * from %s" % dbtable)
    #print("select count = %s", str(cur.rowcount()))
    print(cur.fetchone())
    print(cur.fetchmany(2))
    for row in cur.fetchall():
        print(row)
    print("Done!")
    
def test_mysqldb3():
    cxn = db.connect(host=dbhost, db=dnname, user=dbuser, passwd=dbpass)

    dbtable = "users"
    cxn.query("DROP TABLE IF EXISTS %s" % dbtable)
    cxn.commit()

    cur = cxn.cursor()
    cur.execute('''
            CREATE TABLE users (
                login VARCHAR(8),
                uid INTEGER,
                prid INTEGER)
        ''')

    NAMES = (
        ('aaron', 8312), ('angela', 7603), ('dave', 7306),
        ('davina',7902), ('elliot', 7911), ('ernie', 7410),
        ('jess', 7912), ('jim', 7512), ('larry', 7311),
        ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
        ('serena', 7003), ('stan', 7607), ('faye', 6812),
        ('amy', 7209),
    )
    datas = ((34, '3434'), (56, '5656'))
    def randName():
        pick = list(NAMES)
        while len(pick) > 0:
            yield pick.pop(random.randrange(len(pick)))
    #print("INSERT INTO users VALUES(%s, %s, %s)\n", [(who, uid, random.randrange(1,5)) for who, uid in randName()])
    #dd={234:"#43", 456:"sfdsd"}
    #print([(k,v) for k,v in dd.items()])

    cur.executemany("INSERT INTO users VALUES(%s, %s, %s)",
        [(who, uid, random.randrange(1,5)) for who, uid in randName()])

    cur.execute("select * from %s" % dbtable)
    print(cur.fetchone())
    for row in cur.fetchall():
        print(row)
        
if __name__ == "__main__":
    print("---------------")
    test_mysqldb1()
    print("---------------")
    test_mysqldb2()
    print("---------------")
    test_mysqldb3()