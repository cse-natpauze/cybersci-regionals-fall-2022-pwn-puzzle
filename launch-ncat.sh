#!/bin/bash

socat TCP4-LISTEN:10001,reuseaddr,fork EXEC:"stdbuf -oL ./main" 

#connect with netcat `nc`, `ncat`, etc