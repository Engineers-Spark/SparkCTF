#!/usr/bin/python3 -u

from pwn import *
import os

context.log_level = "critical"

r = process("./blind")

while (True):
    try:
        print(r.recvuntil(b"> ").decode(), end = "")

        data = os.read(0, 1024)

        r.send(data)

        try:
            os.write(1, r.recv())
        except:
            break
    except:
        break

r.close()
