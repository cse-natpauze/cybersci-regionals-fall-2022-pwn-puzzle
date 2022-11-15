#!/bin/bash
set -e
gcc -ggdb -D DEBUG main.c -o main
gdb main