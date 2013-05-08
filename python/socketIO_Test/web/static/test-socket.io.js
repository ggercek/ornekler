var socket = io.connect('/chat');

socket.on("connect", function(){
    log('baglandi>');
    socket.emit('subscribe' , {'me': 'mynick'});
    log('kayit istegi gonderildi');
});

socket.on("welcome", function(obj){
    log('Merhaba mesaji geldi. Mesaj icerigi:' + obj);
});

socket.on("message", function(obj) {
    log('Yeni mesaj geldi: ' + obj);
});

function log(logstr) {
    document.getElementById('log').value += logstr + '\n';
}