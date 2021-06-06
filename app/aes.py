


# AES CONFIG
# Derive a 256-bit AES encryption key from the password

passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
# print(key)
# print('AES encryption key:', binascii.hexlify(key))
iv = secrets.randbits(256)
