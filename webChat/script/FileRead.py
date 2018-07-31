from script import reverseFileRead

# ファイル行数算出
def num_file():
    return sum( 1 for line in open('data/date.txt') )

# チャットデータ読み込み
def read_data(num, offset):
    date = reverseFileRead.revarse_file_read('data/date.txt', num, offset)
    name = reverseFileRead.revarse_file_read('data/name.txt', num, offset)
    chat = reverseFileRead.revarse_file_read('data/chat.txt', num, offset)

    item = []
    for (date_, name_, chat_) in zip(date, name, chat):
        data = {}
        data['da'] = date_
        data['name'] = name_
        data['chat'] = chat_
        item.append(data)
    return item

