from Crypto.Util.number import long_to_bytes,getPrime
p=getPrime(512)
q=getPrime(512)
n=p*q
for i in flag:
    out.append(pow(i,e,n))
print(f"out={out}")
print(f"n={n}")
print(f"e={e}")