from django.core.management.base import BaseCommand, CommandError
import socket
from server.models import ServerManagement
import tqdm
import os
import ast


class Command(BaseCommand):

    def handle(self, *args, **options):
        s = socket.socket()
        print("Socket Created")
        s.bind(('192.168.88.140', 5001))
        s.listen(4)
        print("waiting for connections")

        while True:
            c, addr = s.accept()
            with c:
                print('Connected by', addr)
                while True:
                    try:
                        data = c.recv(1024)
                        ls = ast.literal_eval(data.decode("utf-8"))
                        server_name = ls[0]
                        ip_addr = ls[1]
                        if not ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).exists():
                            processor = ls[2]
                            ram = ls[3]
                            ServerManagement.objects.create(server_name=server_name, ip_addr=ip_addr, ram=ram,
                                                            processor=processor, enable=True)
                        # elif ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).values(
                        #         'enable') is False:
                        #     ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).update(enable=True)
                        else:
                            ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).update(
                                enable=True)
                    except:
                        ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).update(enable=False)
                        break

            # print("Connected with ", addr)
            # c.send(bytes("Welcome to my Server", "utf-8"))
            # data = c.recv(2020)
            # # ls = data.decode("utf-8").strip('][').split(', ')

            # if not ServerManagement.objects.filter(server_name=server_name, ip_addr=ip_addr).exists():
            #     processor = ls[2]
            #     ram = ls[3]
            #     ServerManagement.objects.create(server_name=server_name, ip_addr=ip_addr, ram=ram,
            #                                     processor=processor, enable=True)
            # else:
            #     if addr is not None:
            #         print(ls)
            #     else:
            #         print("host is lost!")
