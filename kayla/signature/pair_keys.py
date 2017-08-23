import base64
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA


def import_rsa_key(key_file):
    content = open(key_file).read()
    return RSA.importKey(content)


def sign(rsa_pri_key_file, data):
    rsa_pri_key = import_rsa_key(rsa_pri_key_file)
    sig_maker = PKCS1_v1_5.new(rsa_pri_key)
    h = SHA.new(data.encode('utf-8'))
    sign = sig_maker.sign(h)
    return base64.b64encode(sign)


def verify(rsa_pub_key_file, data, sig):
    rsa_pub_key = import_rsa_key(rsa_pub_key_file)
    verifier = PKCS1_v1_5.new(rsa_pub_key)
    h = SHA.new(data.encode('utf-8'))
    sig = sig.decode('base64')
    return verifier.verify(h, sig)