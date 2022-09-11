from Crypto.Hash import HMAC, SHA256

secret = bytes.fromhex('2712A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')

#Generación
msg0= bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'utf-8')
h = HMAC.new(secret, msg=msg0, digestmod=SHA256)

print(h.hexdigest())
mac = h.hexdigest()

#Verificación
h2 = HMAC.new(secret, digestmod=SHA256)
msg = bytes('Siempre existe más de una forma de hacerlo, y más de una solución válida.', 'utf-8')
h2.update(msg)
try:
  h2.hexverify(mac)
  print("Mensaje validado ok")
except ValueError:
  print("Mensaje validado ko")


  #Solución: d0b686743822793fb185263f1fa4ded09bd557bcd341ac53e06dad76238c8e09 
  # Mensaje validado ok