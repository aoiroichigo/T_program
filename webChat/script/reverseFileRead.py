import subprocess

# ファイル内容を逆から取得する関数
# 参考:http://code.i-harness.com/ja/q/213e8
# [Input]
#   filename:ファイル名
#   num:取得行数
#   offset:最後の行からのオフセット
# [Output]
#   list
def revarse_file_read(filename:str, num, offset=0):
    lists = subprocess.Popen(['tail', '-n', str(num + offset), filename], \
            stdout=subprocess.PIPE) \
            .stdout.read().decode('utf-8').splitlines()
    return lists[:len(lists)-offset]

if __name__ == '__main__':
    filename = 'hoge.txt'

    print('20行のファイルを作成')
    with open(filename,'w') as f:
        for i in range(20):
            f.write(str(i) + "\n")

    print('最後から5行前の以上の行を5行取得')
    lists = revarse_file_read(filename,5,5)
    for line in lists:
        print(line)

    print('最後から5行前の以上の行を20行取得')
    lists = revarse_file_read(filename,20,5)
    for line in lists:
        print(line)

