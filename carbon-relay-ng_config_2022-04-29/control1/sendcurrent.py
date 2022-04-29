#!/usr/local/bin/python
import os
import time
import pickle
import struct
import socket
from pprint import pprint as pp

CARBON_SERVER = '10.0.0.62'
CARBON_PORT = 2004

# DATASOURCE = 'C:/Users/Greg Leblanc/PycharmProjects/OUALGraphing/data/2020-01/'
DATASOURCE = '/home/carter/'

pattern = '%d/%m/%Y-%H:%M:%S'
all_data = []
tandem_files = []

with open(DATASOURCE + 'tandem.time', 'rb') as time_file:
    time_file.seek(-2, os.SEEK_END)
    while time_file.read(1) != b'\n':
        time_file.seek(-2, os.SEEK_CUR)
    current_time = time_file.readline().decode()
    current_time = current_time.rstrip('\r\n')
    epoch = int(time.mktime(time.strptime(current_time, pattern)))

try:
    for entry in os.walk(DATASOURCE):
        for file_name in entry[2]:
            full_path_name = os.path.join(entry[0], file_name)
            if full_path_name.startswith(os.path.join(DATASOURCE, "tandem.")):
                if file_name != "tandem.time" and \
                        file_name != "tandem.now" and \
                        file_name != "tandem.time_previous" and \
                        file_name != "tandem.data" :
#                    print(file_name)
#                    print(full_path_name)
                    tandem_files.append(full_path_name)
                    list([ data_file for data_file in open(full_path_name, 'rt')])[-1]
                    data_entry = data_file.rstrip('\r\n')
                    all_data.append((file_name,(epoch, data_entry)))
                    # with open(entry[0] + name, 'rb') as data_file:
                    #     data_file.seek(-2, os.SEEK_END)
                    #     while data_file.read(1) != b'\n':
                    #         data_file.seek(-2, os.SEEK_CUR)
                    #     data_entry = data_file.readline().decode()
                    #     data_entry = data_entry.rstrip('\r\n')
                    #     all_data.append((name, (epoch, data_entry)))
except StopIteration:
    print('Failed to read data on file', name)

#print(all_data)

payload = pickle.dumps(all_data, protocol=2)
header = struct.pack("!L", len(payload))
message = header + payload
sock = socket.socket()
sock.connect((CARBON_SERVER, CARBON_PORT))
sock.sendall(message)
sock.close
all_data = []
