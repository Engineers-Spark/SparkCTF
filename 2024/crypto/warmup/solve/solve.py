import fractions
from Crypto.Util.number import long_to_bytes


def continued_fraction(e, n):
    while n:
        a = e // n
        yield a
        e, n = n, e - a * n


def convergents(cf):
    n1, n2 = 1, 0
    d1, d2 = 0, 1

    for q in cf:
        n = q * n1 + n2
        d = q * d1 + d2
        yield (n, d)
        n2, n1 = n1, n
        d2, d1 = d1, d


def integer_square_root(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# Function to perform Weiner's attack
def weiners_attack(e, n):
    for k, d in convergents(continued_fraction(e, n)):
        if k == 0 or (e * d - 1) % k != 0:
            continue

        phi_n = (e * d - 1) // k
        s = n - phi_n + 1

        # Solving quadratic equation x^2 - s*x + n = 0
        discr = s * s - 4 * n
        if discr < 0:
            continue

        # Check if discriminant is a perfect square
        sqrt_discr = integer_square_root(discr)
        if sqrt_discr * sqrt_discr != discr:
            continue

        p = (s + sqrt_discr) // 2
        q = (s - sqrt_discr) // 2

        if p * q == n:
            return d
    return None


def decrypt_rsa(ciphertext, e, n):
    d = weiners_attack(e, n)
    if d is not None:
        decrypted_message = pow(ciphertext, d, n)
        return long_to_bytes(decrypted_message).decode('utf-8')
    else:
        return "Failed to decrypt using Weiner's attack"


if __name__ == "__main__":
    ciphertext = 33663628920063164127958463115721595459196664364065461255621218176212192927961718931231149729112068060373232052665460108691322983193566842293944631893405889198100640352350616046165590663181836944218842912056093236951875908070297174785481521641276336898219575613023494568777573477929306135879759007167134718332
    n = 101348626669525492075426920118996224985876048913831079405628361169483461586140162188947564401826696465734519658195042245116513300956895436184905652233964980789552690180246371819650561411861907070763698884358042688682276642540668217228147962300065961009987284153023156529947558899291375280163214068080487969531
    e = 29516316584730232365218427565881140673644824428829443167552125955876494191540383234867551023180853835816547737434278864555500759541444990033696029724307187216618412685714948693804403322981692642012837446348736540221695628887632677504626987457918799931699151998501902764930131206388060245839103526737362000667

    decrypted_message = decrypt_rsa(ciphertext, e, n)
    print("Decrypted message:", decrypted_message)

