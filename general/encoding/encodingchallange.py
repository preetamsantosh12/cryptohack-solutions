### this program just runs till the flag is recieved and abruptly ends , 
### check the console for the flag

import json
from pwn import *  # pip install pwntools
from base64 import b64decode
import codecs
def rot13(s): return codecs.getencoder("rot-13")(s)[0] # from stackoverflow


r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()
while received  is not None:

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])
    recValue = received["encoded"]
    recType = received["type"]

    if recType == "hex":
        to_send = {
            "decoded": unhex(recValue).decode()
        }
    elif recType == "base64":
        to_send = {
            "decoded": (b64decode(recValue).decode())
        }
    elif recType == "utf-8":
        finalstring = ""
        for i in recValue:
            finalstring += chr(i)

        to_send = {
            "decoded":  finalstring
        }
    elif recType == "bigint":
        recValue = recValue[2:]
        to_send = {
            "decoded": unhex(recValue).decode()
        }
    elif recType == "rot13":
        to_send = {
            "decoded": codecs.decode(recValue, 'rot_13')
        }


    json_send(to_send)

    received =  json_recv()