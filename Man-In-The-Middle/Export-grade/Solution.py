# calc the shared secret using the B (bob public key) and the alice secret (that we just bruteforced)
p = 16007670376277647657                    # 0xde26ab651b92a129
B = 5186048199859570232                     # 0x47f88b5c64af0638
a = 3694381458720902541

shared_secret = pow(B,a,p)
print("The shared secret is: ",shared_secret)

# ---------------------------------------------------------------------------------------------------------

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


shared_secret = 14861390263736079937
iv = '1907d1596c363fdd9799e5ca3fcffd41'
ciphertext = '23019aa4ef6e2b6d2f37644174357aab725a9a8b84cd9f48e5dd18940eacd5b0'

print(decrypt_flag(shared_secret, iv, ciphertext))