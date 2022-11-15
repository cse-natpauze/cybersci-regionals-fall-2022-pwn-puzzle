#!/bin/bash
set -e
gcc -D PREPPUZZLE -D DEF_S1=\"TEST\" main.c -o main
./main