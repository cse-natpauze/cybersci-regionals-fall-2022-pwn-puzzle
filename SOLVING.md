


Here is a rough outline of the steps someone could take to solve this:

I expect students to play around with it locally. Read the source. Connect to the remote version and mess around with it.

eventually grasping an understanding of the simple string storage buffer 

> The model service built from `main.c` allows a user to `add`, `remove` and `search` user inputted strings. The string storage is backed by a single continuous section of memory, with a simple linked list structure for tracking allocations in the buffer.

also noticing the search function doesn't actually work

the search function can be identified as a way to get a 1 byte compare off the end of a stored string

> The `search` function has an intentionally introduced bug which causes it to extend the string compare in the search 1 byte beyond the end of each string entry.
The `search` functionality, will not search properly but can be abused to craft a one byte out of bounds compare from a known string. Combined with the `add` (and optionally `remove`) functions, the bug can be crafted into a full string leak to recover a the secret ctf key from the programs memory. 


then crafting an exploit that "grooms" the storage structures in the linked list, and repeatedly uses the search function to leak the challenge key 

an example POC exploit is in poc.py


