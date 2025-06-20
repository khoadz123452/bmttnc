import ecdsa
import os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()

        with open('cipher/ecc/keys/privatekey.pem', 'wb') as f:
            f.write(sk.to_pem())
        with open('cipher/ecc/keys/publickey.pem', 'wb') as f:
            f.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privatekey.pem', 'rb') as f:
            sk = ecdsa.SigningKey.from_pem(f.read())
        with open('cipher/ecc/keys/publickey.pem', 'rb') as f:
            vk = ecdsa.VerifyingKey.from_pem(f.read())
        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode("ascii"))

    def verify(self, message, signature, public_key):  # ✅ cần có public_key
        try:
            return public_key.verify(signature, message.encode("ascii"))
        except ecdsa.BadSignatureError:
            return False
