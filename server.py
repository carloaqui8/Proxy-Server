import socket
from http import server
import requests
import sys
import argparse

BUFF_LEN = 1024

if __name__ == '__main__':
    try:
        HOST = '127.0.0.1'
        PORT = 3000

        s = socket.socket()
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            print(conn, addr)
            data = conn.recv(BUFF_LEN)
            if data:
                print(data.decode())
                conn.send('wahaha'.encode())

    except Exception as e:
        s.close()
        print(e)
