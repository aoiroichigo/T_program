# webChat
flaskを利用したwebチャットアプリ<br>
機能：アカウントの作成，ログイン，チャット


## Install
### flask
> pip3 install Flask

### mySQL
> sudo apt install mysql-server mysql-client

### python & mySQL
> sudo apt-get install python3-pip
> python3 -m pip install PyMySQL


## How to use
### データベース作成
以下の"testdb"は自由に変更すること<br>
<br>
mysqlの立ち上げ<br>
> mysql -u root -p
<br>
データベースの作成<br>
> mysql> create database testdb;
<br>
テーブルの作成<br>
> mysql> create table testdb.login(number int(10) primary key auto_increment, id char(20), passwd char(129));
<br>
作成したテーブルの確認<br>
> mysql> show fields from testdb.login;<br>
<br>

### 利用するデータベースの設定方法
データフォルダ内に設定ファイルである"db.ini"が存在する<br>
この中のデータベース名などを変更する
<br>

### 起動方法
> python3 web.py
