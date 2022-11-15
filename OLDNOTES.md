## old notes I made prior to implementation
idea: 
a small remote app (or even local if i can just get a shell to intereact with its in/out?)
stores input string in a linked list 
possibly in one continuous mem region to make this simpler?
typical one byte OOB compare/read with a bad for loop

you can remove string entries. witch patches them out of the linked list but doesnt 0 the mem
you can also querry strings and it will tell you if any match

goal is to steal a string


ex:
strings preloaded
string 1 
string 2
string 3 
target string 

string 1 2 and 3 are known 
target string is unknown

target string is "logged out" automatically

goal is to log out string 3, then make string a new string 3 
by searching for if the new string 3 + looping through 0x00-0xff byte we can find first byte of target string 
repeat with string 3 + known first byte + looping through 0x00-0xff byte untill you get all the bytes of the string 
