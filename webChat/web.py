import os.path
import sys
import math
import datetime

from flask import Flask, render_template, session, request, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect

import json
from xml.sax.saxutils import unescape

from script import FileRead
from script import Login
from script import Hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!' # cookie を暗号化する秘密鍵 (本来はランダムに作る)

socketio = SocketIO(app)
thread = None

def log_w(act:str):
    now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    name = ""
    if session.get('username') is not None:
        name = session['username']

    with open('data/log.txt','a') as f:
        f.write(now + "," + act + "," + name + "\n")

@app.route('/')
def index()->str:
    if session.get('username') is not None:
        session.pop('username', None)

    log_w('connect')
    return render_template('home.html')

###############
## ホーム画面 ##
###############
@app.route('/home', methods=['POST'])
def home()->str:
    res = request.form['button']
    if res == 'Login':
        log_w('in login')
        return render_template('login.html')
    else:
        log_w('in signUp')
        return render_template('signUp.html')

#################
## ログイン画面 ##
#################
@app.route('/login', methods=['POST'])
def login():
    ID = request.form['ID']
    passwd = request.form['passwd']

    passwd = Hash.hash(passwd) # ハッシュ値に変換

    if not ID or not passwd:
        log_w('login error')
        login_result = False
    else:
        log_w('login success')
        login_result = Login.sql_login(ID,passwd) # ログインの確認

    if login_result:
        session['username'] = str(ID)
        num_page = math.ceil(FileRead.num_file()/10)
        item = FileRead.read_data(10, 0)

        if num_page == 0:
            num_page = 1
        elif num_page > 5:
            num_page = 5

        log_w('in chat')
        return render_template('chat_main.html', page=1, pages=range(1,num_page+1), DATA=json.dumps(item))
    else:
        return render_template('login.html',login_error="true")

#####################
## サインアップ画面 ##
#####################
@app.route('/signUp', methods=['POST'])
def signUP():
    Id = request.form['Id']
    Pass = request.form['Pass']

    if not Id or not Pass:
        log_w('signUp error')
        return render_template('signUp.html', error="false")

    Pass = Hash.hash(Pass)

    if Login.sql_sign_up(Id,Pass):
        log_w('signUp success')
        return render_template('home.html')
    else:
        log_w('signUp error')
        return render_template('signUp.html', error="false")

###############
## chat_main ##
###############
# チャットページ切り替え
@app.route('/chat_change', methods=['POST'])
def change_page():
    log_w('chat change')

    num_page = math.ceil(FileRead.num_file()/10)
    change_page = request.form['page_num']

    res = 0
    if change_page == "start":
        res = 1
    elif change_page == "end":
        res = num_page
    else:
        res = int(change_page)

    item = FileRead.read_data(10, res*10-10)

    print(num_page)

    tmp = []
    if num_page < 4:
        tmp = range(1,num_page+1)
    else:
        if res < 3:
            tmp = range(1,6)
        elif res < num_page-2:
            tmp = range(res-2,res+3)
        else:
            tmp = range(num_page-4,num_page+1)

    return render_template('chat_main.html', page=res, pages=tmp, DATA=json.dumps(item))

# ユーザーデータ付与
# コメント内容保存
@socketio.on('my_event', namespace='/chat_req')
def test_broadcast_message(msg):
    log_w('chat speak')

    n = session['username'].encode('unicode_escape').decode().replace('\\', '%')

    with open('data/date.txt','a') as f:
        f.write(msg['da'] + "\n")
    with open('data/name.txt','a') as f:
        f.write(n + "\n")
    with open('data/chat.txt','a') as f:
        f.write(msg['chat'] + "\n")

    emit('my_response',{'name':n, 'da': msg['da'], 'chat': msg['chat']},broadcast=True)

if __name__ == '__main__':
    if not os.path.exists("data/db.ini"):
        print("データベースの設定ファイルがありません")
        print("「db.ini」を作成してください")
        sys.exit()

    # ない場合エラーになるので，作成しておく
    if not os.path.exists("data/date.txt"):
        with open('data/date.txt','w') as f:
            pass
    if not os.path.exists("data/name.txt"):
        with open('data/name.txt','w') as f:
            pass
    if not os.path.exists("data/chat.txt"):
        with open('data/chat.txt','w') as f:
            pass

    #app.debug=True
    app.run(host='0.0.0.0', port=8080)

