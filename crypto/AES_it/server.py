import socket
import os
import sys
import traceback
import random
import time
from Crypto.Cipher import AES
import socketserver
from threading import Thread
from secret import FLAG, KEY

PORT = int(os.environ.get("PORT", 6955))

aes = AES.new(KEY, AES.MODE_ECB)

MENU = b"""
Select:
    1) Encrypt with flag(Stronger and Secure)
    2) Encrypt
Your choice: """

def pad(s):
    if len(s) % 16 == 0:
        return s
    else:
        pad_b = 16 - len(s) % 16
        return s + bytes([pad_b]) * pad_b

def encrypt(conn):
    while True:
        conn.sendall(MENU)
        choice = conn.recv(1024).strip()

        if choice == b'1':
            conn.sendall(b'Enter your message:\n> ')
            inp = conn.recv(1024).strip()
            enc = aes.encrypt(pad(inp + FLAG.encode()))
            conn.sendall(b"\nEncrypted input\n" + enc.hex().encode() + b"\n")
        elif choice == b'2':
            conn.sendall(b'Enter your message:\n> ')
            inp = conn.recv(1024).strip()
            enc = aes.encrypt(pad(inp))
            conn.sendall(b"\nEncrypted input\n" + enc.hex().encode() + b"\n")
        else:
            conn.sendall(b"\nOhhh eeesyyy no Hacking here !!!\n")
            

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    BANNER = """ 
 █████╗ ███████╗███████╗    ██╗████████╗
██╔══██╗██╔════╝██╔════╝    ██║╚══██╔══╝
███████║█████╗  ███████╗    ██║   ██║   
██╔══██║██╔══╝  ╚════██║    ██║   ██║   
██║  ██║███████╗███████║    ██║   ██║   
╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝   ╚═╝        
 """.encode()


    MESSAGE = b"""
Hello there!!! Just so you know we use a super strong
encryption algorithm called AES ECB, to prevent hackers
to access your data. If you wanna check, go ahead and try
to get the flag

There are two options in this challenge!!!
- The first one is to encrypt your message by appending
the flag to your plaintext input and encrypting it
- The second method is to encrypt your message just by using 
plaintext

Press Enter to continue: """

    conn.sendall(BANNER)
    conn.sendall(MESSAGE)

    while True:
        input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)

        siz = sys.getsizeof(input_from_client_bytes)
        if  siz >= MAX_BUFFER_SIZE:
            print("The length of input is probably too long: {}".format(siz))

        encrypt(conn)

    conn.close()
    print('Connection ' + ip + ':' + port + " ended")

def start_server():
    
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("0.0.0.0", PORT))
        print('Socket bind complete')
    except socket.error as msg:
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()

    soc.listen(10)
    print('Socket now listening')

    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            traceback.print_exc()
    soc.close()

start_server()  