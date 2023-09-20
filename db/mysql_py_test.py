# codig=utf8
import MySQLdb


def test_select():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456')
    conn.select_db('rsdk')
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    curs.execute('select * from game where gameId = "1"')
    results = curs.fetchall()
    for r in results:
        print r['gameId']
    conn.close()


def insert_data():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db="pick_pearl", charset="utf8")
    conn.autocommit(1)
    cursor = conn.cursor()
    sql = "insert into w3school_page(title,link,msg_desc,status) values ('" + 'tt' + "','" + 'baidu' + "','" + 'desc' + "', '1')"
    print sql
    print cursor.execute(sql)
    #conn.commit()


insert_data()
