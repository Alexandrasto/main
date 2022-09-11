import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


clave_bytes = bytes.fromhex('e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72')

iv_bytes = bytes.fromhex('00000000000000000000000000000000')
dato_cifrado = ("zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNIosyKfkNKG9GGSgG1awaZg==")
dato_cifrado_bytes = b64decode(dato_cifrado)
cifrado = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
# Desciframos
dato_desc_bytes = cifrado.decrypt(dato_cifrado_bytes)
# Quitar el padding
dato_descifrado_unpad_bytes = unpad(dato_desc_bytes, AES.block_size,style="pkcs7")

print("En hex: ", dato_desc_bytes.hex())
print("El texto en claro es: ", dato_desc_bytes.decode("UTF-8"))

#Solucion En hex:  4573746f20657320756e206369667261646f20656e20626c6f7175652074c3ad7069636f2e20526563756572646120656c2070616464696e672e060606060606
#El texto en claro es:  Esto es un cifrado en bloque típico. Recuerda el padding.
