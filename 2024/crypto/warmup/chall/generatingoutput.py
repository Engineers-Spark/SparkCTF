from Crypto.Util.number import getPrime, inverse

def generate_vulnerable_key(bitsize):
    """Generates RSA parameters (n, e) vulnerable to Wiener's attack."""
    p = getPrime(bitsize)
    q = getPrime(bitsize)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a small d
    d = getPrime(20)
    e = inverse(d, phi)
    
    return n, e

def encrypt(message, e, n):
    """Encrypts a message using RSA encryption."""
    m = bytes_to_long(message.encode())
    c = pow(m, e, n)
    return c

def bytes_to_long(bytes_data):
    """Converts bytes to a long integer."""
    return int.from_bytes(bytes_data, byteorder='big')

# Key Generation
n, e = generate_vulnerable_key(512)

# Encryption - The message is not provided to the players
message = "SparkCTF{B451C_R54_T45K}"  # This should be the plaintext message you want encrypted
ciphertext = encrypt(message, e, n)

# Output the challenge data
print("Public Key (n, e): ", (n, e))
print("Ciphertext: ", ciphertext)
