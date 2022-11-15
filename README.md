# string-storage CTF puzzle for CYBERSCI regionals Fall 2022

This directory contains the development artifacts and deliverables for string-storage, a CTF puzzle I was tasked with creating.
 - Nathaniel Pauzé - October 2022

## THESIS:

"String-Storage is a memory corruption and memory shaping ctf puzzle aimed at beginners. Without needing any knowledge of debuggers or memory allocators, they will identify a single byte out-of-bounds string compare, and with some basic memory grooming craft it into a string leak to recover the puzzle key from a remote service"


string-storage is an introductory level puzzle aimed at university students. However its novelty will _hopefully_ require even experienced CTF'ers to "go back to basics" to manually craft a successful exploit. 

Solving is expected to take less than 30 min for someone experienced up to 1 hour for those less experienced. 

## Details

The model service built from `main.c` allows a user to `add`, `remove` and `search` user inputted strings. The string storage is backed by a single continuous section of memory, with a simple linked list structure for tracking allocations in the buffer.

The `search` function has an intentionally introduced bug which causes it to extend the string compare in the search 1 byte beyond the end of each string entry.
The `search` functionality, will not search properly but can be abused to craft a one byte out of bounds compare from a known string. Combined with the `add` (and optionally `remove`) functions, the bug can be crafted into a full string leak to recover a the secret ctf key from the programs memory. 

## Distributing and Deploying

Build a release version of the `main` binary using the [build-release-puzzle-prep.sh](build-release-puzzle-prep.sh) script. This binary will not print debugging output, and will contain the target ctf key defined by the `CTFKEY` variable passed to the compiler. DO NOT DISTRIBUTE THIS BINARY OR BUILD SCRIPT TO COMPETITORS

The [launch-ncat.sh](launch-ncat.sh) script is intended to be bundled into a VM or a container along side the `main` binary from the step above. Make the script run on container/VM start up. When a new connection is received on port 10001, the `main` binary will start up, and expose its stdin and stdout over the socket (flushing on newlines). This is how participants will interact with the puzzle. 

The source code in [main.c](main.c) SHOULD BE DISTRIBUTED TO PARTICIPANTS. (Note: removing the dumpHex function from the source could be done to encourage students to leverage a debugger for understanding the program) 

I've provided a small intro text for use on CTFd or another platform. A sample of this text can be found at [SAMPLE_CALLENGE_TEXT.md](SAMPLE_CALLENGE_TEXT.md)

















