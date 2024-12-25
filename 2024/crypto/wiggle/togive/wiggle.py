#! /usr/bin/env python3

#!/usr/bin/env python3

"""
Author : msalaani
Task : Wiggle - Task
Event : SparkCTF

"""

from Crypto.Util.number import bytes_to_long
import os

try:
	from secret import FLAG
except ImportError:
	FLAG = b"SparkCTF{50M3_L33t_5tr1nG}"

def encrypt(msg, keystream):
    return bytes(msg_ ^ next(keystream) for msg_ in msg)

def StreamKeyGen(state):
	while 1:
		yield state & 0xff
		for _ in range(16):
			bit = ((state >> 64) * (state >> 62) * (state >> 61) ^ (state >> 60) - (state >> 57) + (state >> 55) + (state >> 53) ^ (state >> 51) ^ (state >> 50) ^ (state >> 49) + (state >> 46) ^ (state >> 45) * (state >> 44) + (state >> 43) ^ (state >> 40) + (state >> 38) * (state >> 37) + (state >> 36) ^ (state >> 35) - (state >> 31) + (state >> 29) - (state >> 28) - (state >> 26) - (state >> 23) + (state >> 17) ^ (state >> 16) + (state >> 14) + (state >> 9) * (state >> 3) * (state >> 2) + state) & 1
			state = (state >> 1) | (bit << 63)


def main():
    print("Welcome to SparkCTF 2024 - Wiggle challenge !")
    print("Give me a message and I'll encrypt it for you with my super duper secure encryptor, with a gift at the end")
    
    my_super_secret_seed = bytes_to_long(os.urandom(8))
    keystream = StreamKeyGen(my_super_secret_seed)
    
    
    try:
        user_msg = bytes.fromhex(input("Your message (hex): "))
        assert len(user_msg) <= 10 and not b"\x00" in user_msg
        encrypted_user_message = encrypt(user_msg + FLAG, keystream).hex()
        print(f"Here is your thing: {encrypted_user_message.hex()}")
        
    except :
        print("Bad boy! Bye.")
        exit()

if __name__ == "__main__":
    main()
