#!/bin/bash
set -e
gcc -ggdb -D DEBUG -D PREPPUZZLE -D CTFKEY=\"this-is-the-ctf-puzzle-key-here-in-memory\\n\" main.c -o main
gdb main