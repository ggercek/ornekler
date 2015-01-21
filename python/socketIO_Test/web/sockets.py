from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin
from socketio.sdjango import namespace

client = 0

@namespace('/chat')
class ChatNamespace(BaseNamespace, BroadcastMixin):

    def on_subscribe(self, msg):
        global client
        client += 1

        print 'yeni kullanici: ', msg
        self.emit('welcome', '%d numarali istemcisiniz.'%(client))
        self.emit('message', 'socketIO_Test projesinden bir mesaj geldi... %d'%(client))

    def on_update(self, msg):
        print 'guncelleme bilgisi geldi. ', msg
        self.emit('message', msg)
