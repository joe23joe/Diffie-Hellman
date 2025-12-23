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


shared_secret = 0xca3716d375c1bfeacec51cedddb4f4c5f6144afd0db7da4fa95c8106f3c025c5b79a3147f072ffef482950327285e54b0d4a0ac5c9df4510a9a2e5e8cd3af88864217252f14696c40ada45de537c3a2cde7a2238790a133f5d5aef28833a625e9c19ebd054b111de6c1c2935e87cd55d9ef5de40daa056ba526fb6663b4001d3a6112c8e9af384b4ce7a7bbbae2af7769afdc343905206dafdd35a55ab6436bd9460f25d25e6ca269cd7a57b979e9c044a378b8876d9f09baa88bfb646cb68e0
iv = 'ee8f37ef26498c4ebacb3fe6265eddca'
ciphertext = 'f849a02781dc16aa31cd1ac43ed9ae0506d403613a972a8a398e54d7f8dd694faaf87756364a9a75025afdff3827f071874d616f8b696d4b98f21d4de9dafca43b2f090db5e68c72c4f6907bb0a44099'

print(decrypt_flag(shared_secret, iv, ciphertext))