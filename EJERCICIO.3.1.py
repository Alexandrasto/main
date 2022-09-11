from Crypto.Cipher import ChaCha20 
from base64 import b64decode, b64encode


#Cliente 
textoPlano_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado', 'UTF-8')
clave = bytes.fromhex('979df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120')
nonce_mensaje = bytes.fromhex('f5871c9ff7f99c926102dd92')
print('nonce  = ', nonce_mensaje.hex())



cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())


#Descifrado...
decipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
plaintex_bytes = decipher.decrypt(texto_cifrado_bytes)
print('Mensaje en claro = ',plaintex_bytes.decode('utf-8'))

