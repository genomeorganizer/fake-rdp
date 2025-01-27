#!/usr/bin/python
"""Fake RDP Server"""
import socket
import time
import json
import os
from getmac import get_mac_address
from os.path import expanduser
home = expanduser("~")
default_path=os.path.join(home,".mail")
import email_alerts

def load_auth_file(filename):
    with open(filename, "r") as auth_file:
        auth = json.load(auth_file)
        return auth

def fake_server():
    """Start a socket on port 3389 and send init packets"""
    #a=load_auth_file("/usr/local/bin/email.json")
    a=default_path
    email_alerts.send(auth=a,to=a['to'],subject="Fake RDP Server started",message="Started fake RDP server")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 3389))
    serversocket.listen(5)
    while True:
        try:
            connection, address = serversocket.accept()
            mac = get_mac_address(ip=str(address[0]))
            msg='Recieved connection from ip: {} port: {} mac: {}'.format(address[0],address[1],mac)
            print(msg)
            connection.recv(256)
            # Init packet of an NLA-enabled RDP server
            bts = bytearray.fromhex('030000130ed000001234000209080002000000')
            connection.send(bts)
            connection.recv(256)
            bts = 'arbitrary string'
            # Wait before sending a response (resulting in a client-side error)
            print("Sending email alert")
            try:
                email_alerts.send(auth=a,to="tosteveayers@outlook.com",subject="RDP Connection attempt detected",message=msg)
                print("Sent email")
            except:
                print("unable to send alert")
            time.sleep(2)
            connection.send(bts.encode())
        except Exception:
            pass


if __name__ == "__main__":
    fake_server()
