import socket, time                   # Import socket module

#print("120 saniye bekleniyor")
#time.sleep(120)

try:
    port = 9090                # Reserve a port for your service every new transfer wants a new port or you must wait.
    s = socket.socket()             # Create a socket object
    host = "192.168.10.212"   # Get local machine name
    s.connect((host, port))              # Now wait for client connection.

    print('Client dinleniyor....')

    filename='C:/Users/boyut/Desktop/open.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        s.send(l)
        print('Gönderildi: ', repr(l))
        l = f.read(1024)
    f.close()
    print("Dosya gönderildi")
    time.sleep(30)
except Exception as e:
    print(e)
