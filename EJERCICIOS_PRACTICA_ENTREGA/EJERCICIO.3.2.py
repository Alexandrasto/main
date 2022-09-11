from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:

    textoPlano_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado”', 'UTF-8')
    clave_bytes = bytes.fromhex('979df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120')
    nonce_mensaje_bytes = get_random_bytes(12)
    datos_asociados_bytes = bytes('Datos no cifrados sólo autenticados', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_mensaje_bytes)
    cipher.update(datos_asociados_bytes)
    texto_cifrado_bytes, tag_bytes = cipher.encrypt_and_digest(textoPlano_bytes)
    mensaje_enviado = { "nonce": b64encode(nonce_mensaje_bytes).decode(),"datos asociados": b64encode(datos_asociados_bytes).decode(), "texto cifrado": b64encode(texto_cifrado_bytes).decode(), "tag": b64encode(tag_bytes).decode()}
    json_mensaje = json.dumps(mensaje_enviado)
    print("Mensaje: ", json_mensaje)


    #Descifrado...

    tag_2 = b64decode("f5871c9ff7f99c926102dd92")
    decipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=b64decode(mensaje_enviado["nonce"]))
    decipher.update(b64decode(mensaje_enviado["datos asociados"]))
    plaintext_bytes = decipher.decrypt_and_verify(b64decode(mensaje_enviado["texto cifrado"]),b64decode(mensaje_enviado["tag"]))
    print('Datos cifrados en claro = ',plaintext_bytes.decode('utf-8'))
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)