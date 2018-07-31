// 時間の取得
function date_(){
    var now = new Date();
    var Y = now.getYear();     if(Y < 2000){ Y += 1900;     } // 年
    var M = now.getMonth()+1;  if(M < 10)  { M  = "0" + M;  } // 月
    var D = now.getDate();     if(D < 10)  { D  = "0" + D;  } // 日
    var HH = now.getHours();   if(HH < 10) { HH = "0" + HH; } // 時
    var MM = now.getMinutes(); if(MM < 10) { MM = "0" + MM; } // 分
    var SS = now.getSeconds(); if(SS < 10) { SS = "0" + SS; } // 秒
    return Y + '/' + M + '/' + D + ' ' + HH + ':' + MM + ':' + SS;
}

// チャット文の表示
function print(msg){
    $('#log').prepend(
        '<div class="print_chat" style="border:#ff0000 solid 1px;">' +
            '<div style="width:100%; float:left; background-color:#90ddb4;">' +
                msg.da + '&nbsp;' + unescape(msg.name) +
            '</div>' +
            '<div>' +
                '<br>' + unescape(msg.chat) +
            '</div>' +
        '</div>'
    );
}

