import pymysql
import configparser
import os
import sys
def sql_connect():
    """
    mysqlとの接続を行う
    返り値として接続情報を返す
    """

    dataBase = 'testdb02'
    config = configparser.ConfigParser()
    if os.path.exists("data/db.ini"):
        config.read("data/db.ini", encoding='utf8')
    else:
        print('not found database')

    connector = pymysql.connect(host    = config.get('DBSetting', 'host'),
                                db      = config.get('DBSetting', 'dataBase'),
                                user    = config.get('DBSetting', 'user'),
                                passwd  = config.get('DBSetting', 'passwd'),
                                charset = config.get('DBSetting', 'charset') )
    return connector

def sql_login(id, passwd)->bool:
    """
    login用の関数
    データベース内にユーザー情報が存在するか確認する
    存在する場合 True を返す
    """
    connector = sql_connect()
    with connector.cursor() as cursor:
        # IDとパスワードが存在するか確認
        sql = "SELECT * FROM login WHERE id REGEXP BINARY %s \
                && passwd REGEXP BINARY %s"
        result = cursor.execute( sql, (id,passwd) )

    connector.close()
    return result

def sql_sign_up(id, passwd)->bool:
    """
    sign in 用関数
    データベース内にIDが存在しない時，ユーザ情報を追加する
    追加した場合 True，追加できなかった場合 False を返す
    """
    connector = sql_connect()
    with connector.cursor() as cursor:
        # データベース上にIDがあるかどうかを判定
        sql = "SELECT * FROM login WHERE id REGEXP BINARY %s"
        if cursor.execute( sql, id ):
            return False

        # データの追加
        sql = 'INSERT INTO login (id,passwd) VALUES(%s,%s)'
        result = cursor.execute( sql, (id, passwd) )
        connector.commit() # コミット

    connector.close()

    return result

if __name__ == "__main__":
    print('ログイン(1) or アカウント作成(2)：',end='')
    YN = input()

    print('アカウントの追加')
    print('IDを入力してください：',end='')
    id = input()
    print('passwordを入力してください:',end='')
    passwd = input()

    if YN == '1':
        login_result = sql_login(id, passwd)
    else:
        login_result = sql_sign_up(id, passwd)

    if login_result:
        print('success')
    else:
        print('error')



