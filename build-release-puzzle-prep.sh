#!/bin/bash
set -e
gcc -D PREPPUZZLE -D CTFKEY=\"this-is-the-ctf-puzzle-key-here-in-memory\\n\" main.c -o main
