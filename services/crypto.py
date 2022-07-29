import random
import string

from Crypto.Cipher import AES
from Crypto.Hash import SHA256


def get_random_chars(length):
    """ return random string like a7GhNed"""
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(char) for x in range(length))


def password_to_key(password):
    """
    Use SHA-256 over our password to get a proper-sized AES key.
    This hashes our password into a 256 bit string.
    """
    return SHA256.new(str.encode(password)).digest()


def encrypt_data(text, password, second_password=None):
    text = text.encode()
    if second_password:
        key = password_to_key(password + second_password)
    else:
        key = password_to_key(password)
    encoder = AES.new(key, AES.MODE_EAX)
    nonce = encoder.nonce
    ciphertext, tag = encoder.encrypt_and_digest(text)

    return nonce + ciphertext + tag


def decrypt_data(encrypted_data, password, second_password=None):
    if second_password:
        key = password_to_key(password + second_password)
    else:
        key = password_to_key(password)
    nonce = encrypted_data[:AES.block_size]
    decrypted_data = encrypted_data[AES.block_size:-AES.block_size]
    tag = encrypted_data[-AES.block_size:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    return cipher.decrypt_and_verify(decrypted_data, tag).decode()


def get_short_id(Fields) -> str:
    """
    Fields - class which describes fields in DB
    Return short id for making short URL. Check and avoid duplicates
    Return >= 3 characters
    """

    length = 3
    attempt = 0

    while True:
        short_id = get_random_chars(length)
        if Fields.objects.filter(pk=short_id).exists():
            attempt += 1
            if not attempt % 3:
                length += 1
        else:
            return short_id
