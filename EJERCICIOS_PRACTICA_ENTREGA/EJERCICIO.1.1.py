from operator import xor
from multiplicar import *
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


#K1 (key manager) ^ K2 (desarrollador) = K (keyStore)



K1= bytes.fromhex('A1EF2ABFE1AAEEFF')
K2= bytes.fromhex('B1AA12BA21AABB12')

K= xor_data(K1,K2)
K_hex = xor_data(K1,K2).hex()

print("K=K1^K2: ", K_hex)

K22 = xor_data(K,K1)

print("K2=K3 ^K1: ", K22.hex())

K1= xor_data(K2,K1)

print("K1=K2 ^ K: ", K1.hex())