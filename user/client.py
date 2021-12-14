
import sys
sys.path.append("..")
import socket
import tqdm
import os
from pathlib import Path
from server.models import ServerManagement



SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver

# the port, let's use 5001
port = 5001
parentdir = Path(os.getcwd())
# the name of file we want to send, make sure it exists
for f in Path(os.path.join(parentdir, 'media')).glob('*.zip'):
    filename = f
# get the file size
filesize = os.path.getsize(filename)

def SendFile(data):

    serverdata = ServerManagement.objects.get(server_name=data)
    print(serverdata.ip_addr)
    # hostdata = data
    # print("I'm coming coming ")
    # print(hostdata)

    # host = "0.0.0.0"
    # s = socket.socket()
    #
    # print(f"[+] Connecting to {host}:{port}")
    # s.connect((host, port))
    # print("[+] Connected.")
    #
    # # send the filename and filesize
    # s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    # # a = "abc"
    # # s.send(bytes(a,'utf-8'))
    #
    # # # start sending the file
    # progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    # with open(filename, "rb") as f:
    #     while True:
    #         # read the bytes from the file
    #         bytes_read = f.read(BUFFER_SIZE)
    #         if not bytes_read:
    #             # file transmitting is done
    #             break
    #         # we use sendall to assure transimission in
    #         # busy networks
    #         s.sendall(bytes_read)
    #         # update the progress bar
    #         progress.update(len(bytes_read))
    # # close the socket
    # s.close()
