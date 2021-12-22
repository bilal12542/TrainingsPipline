
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




def SendFile(data):
    for f in Path(os.path.join(parentdir, 'media')).glob('*.zip'):
        filename = f
    filesize = os.path.getsize(filename)
    serverdata = ServerManagement.objects.get(id=data)
    host = str(serverdata.ip_addr)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    # send the filename and filesize
    s.send(f"{filename}{SEPARATOR}{filesize}".encode('ISO-8859-1'))


    # # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the socket
    s.close()
