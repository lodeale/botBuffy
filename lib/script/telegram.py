import telepot
import time
from lib.models.users import Users
from pprint import pprint
from script import Script

class Telegram(Script):
    _connect = ''
    _instance = None
    _handler = None
    _message = []
    _userOn = None

    def connect(self):
        try:
            self._connect = telepot.Bot('265058909:AAEN0g4PeqXie-AZPfEGmsfQsBEzDkTuUhw')
            pprint(self._connect.getMe())
            return 1
        except (NameError, ValueError):
            print "Error de conexion"
            print str(NameError) + ': ' + str(ValueError)
            return 0

    def auth(self,user,email,name):
            return 1

    def handler(self,msg):
            self._userOn = self._connect.getUpdates()
            pprint(self._userOn)
            content_type, chat_type, chat_id = telepot.glance(msg)
            print(content_type, chat_type, chat_id)
            if content_type == 'text':
                response = self.makeResponse(msg['text'])
                if response:
                    for i in self._message:
                        self._connect.sendMessage(chat_id, i)

    def listening(self):
        self._connect.message_loop(self.handler)
        print '[+]Listening Bot...\n'
        while 1:
            time.sleep(10)

    def makeResponse(self,msg):
        self._message = []
        if ( msg.find("/nespen") != -1 ):
            msg = msg[7:].strip()

        try:
            inputMsg = str(msg).lower()
            #Imprimimos lo que viene del cliente
            print "*"*50
	    #*****************************
	    #Usuario
	    #*****************************
            queryUser = Users.selectBy(user=str(self._userOn[0]['message']['chat']['id']))
            if queryUser.count() == 0:
                print "[+]Save User....\n"
                u = Users(user=str(self._userOn[0]['message']['chat']['id']))
                if u.id > 0 :
                    print "[+]User Save OK!\n"
                else:
                    print "[?]User No Save \n"
            userOn = Users.selectBy(user=str(self._userOn[0]['message']['chat']['id']))[0]
            print "[+]Id: ", userOn.id
            print "*"*50
            #*****************************
	    #servicios
	    #*****************************
            print "findServicesForWord"
            matchServices = self.findServicesForWord(inputMsg)

            for s in matchServices:
                print "Servicio [",s,"]"
                array_message = inputMsg.split(' ')
                result = self.getServices(s, '/'+str(userOn.id)+'/' + ' '.join(array_message))
                print '[+] Imprimiento endpoint y get: ',s, '/'+str(userOn.id)+'/' + ''.join(array_message)
                print "Resultado: ",result
                if result:
                    self._message.append(result)
                else:
                    print "Error en procesar el mensaje o no existe el servicio"
            return True
        except Exception, e:
            print "Error %s " % e
            return False

