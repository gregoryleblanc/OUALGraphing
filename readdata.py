import pickle, socket, struct, time, os, carbon_client

alldata = []
x=0
pattern = '%m/%d/%Y-%H:%M:%S'
with open('C:/tandem_archive_2021-01-01_0101/tandem.time','r') as timefile, open('C:/tandem_archive_2021-01-01_0101/tandem.Air_Receiver','r') as airfile:
    data = airfile.readline()
    while x < 50:
#    while data:
        timestamp = timefile.readline().rstrip('\r\n')
        epoch = int(time.mktime(time.strptime(timestamp,pattern)))
        data = ('AirHeaderPressure',( epoch, airfile.readline().rstrip('\r\n')))
        alldata.append(data)
        x += 1 #delete this one 

print(alldata)

payload = pickle.dumps(alldata, protocol=2)
header = struct.pack("!L", len(payload))
message = header + payload
#print(message)
"""
CARBON_SERVER = 'localhost'
CARBON_PORT = 2004

sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))
sock.sendall(message)
sock.close
"""
