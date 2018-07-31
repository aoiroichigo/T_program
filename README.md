# chatWeb
flaskを利用したwebチャットアプリ
機能：アカウントの作成，ログイン，チャット

## Install
# flask
>> pip3 install Flask

# mySQL
>> sudo apt install mysql-server mysql-client

# python & mySQL
>> sudo apt-get install python3-pip
>> python3 -m pip install PyMySQL

## How to use
# データベース作成
以下の"testdb"は自由に変更すること
mysqlの立ち上げ
>> mysql -u root -p

データベースの作成
mysql> create database testdb;

テーブルの作成
mysql> create table testdb.login(number int(10) primary key auto_increment, id char(20), passwd char(129));

作成したテーブルの確認
mysql> show fields from testdb.login;
+--------+-----------+------+-----+---------+----------------+
| Field  | Type      | Null | Key | Default | Extra          |
+--------+-----------+------+-----+---------+----------------+
| number | int(10)   | NO   | PRI | NULL    | auto_increment |
| id     | char(20)  | YES  |     | NULL    |                |
| passwd | char(129) | YES  |     | NULL    |                |
+--------+-----------+------+-----+---------+----------------+

# 利用するデータベースの設定方法
データフォルダ内に設定ファイルである"db.ini"が存在する
この中のデータベース名などを変更する
