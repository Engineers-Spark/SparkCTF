from Crypto.Util.number import getPrime, bytes_to_long


def encrypt_message_byte_by_byte(message, e, n):
    return [pow(m, e, n) for m in message]


p = getPrime(512)
q = getPrime(512)
n = p * q
e = 65537


message = b'SparkCTF{R54_15_N0t_34SY}'


out = encrypt_message_byte_by_byte(message, e, n)


print(f"out = {out}")
print(f"n = {n}")
print(f"e = {e}")
