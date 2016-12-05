import requests
from Crypto.Cipher import AES



url="http://music.163.com/api/song/detail/?id=28151022&ids=%5B28151022%5D"

res=requests.post(url)
print(res.content)

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext