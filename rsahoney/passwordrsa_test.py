# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py
# work together.

from password import *
from DTE import *
import os
from random import randint
import rsa


''' Create prefixes dictionary 'prefix': [numRandom, cardLength, probWeight]
i.e. 
prefixes = {
    '5235**': [2, 8, 100],
    '123456': [0, 8, 1]
}
'''

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
SEED_SPACE_LENGTH = 64
seed_space = 2**SEED_SPACE_LENGTH - 1



#generate keys
(pubkey, privkey) = rsa.newkeys(1024)
  
pub = pubkey.save_pkcs1()
pubfile = open('public.pem','w+')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('private.pem','w+')
prifile.write(pri)
prifile.close()

# load key
with open('public.pem') as publickfile:
	p = publickfile.read()
	pubkey = rsa.PublicKey.load_pkcs1(p)

with open('private.pem') as privatefile:
	p = privatefile.read()
	privkey = rsa.PrivateKey.load_pkcs1(p)

with open('guessedprivate.pem') as guessedprivatefile:
	p = guessedprivatefile.read()
	guessedprivkey = rsa.PrivateKey.load_pkcs1(p)

def rsa_decrypt(cipher, key):
	if key == privkey:
		return rsa.decrypt(cipher, key)
	start = 0
	end = seed_space - 1
	seed = int(random.random() * (end-start) + start)
	return seed

pwd_example = '567890'


# Create probability fxns
id_fxns = TelNOProbabilityFxns()


# Use DTE on identification example
seed = encode(pwd_example, id_fxns)

ciphertext = rsa.encrypt(str(seed), pubkey)
decipher_seed = rsa_decrypt(ciphertext, privkey)


seed_guessedkey =  rsa_decrypt(ciphertext, guessedprivkey) 

print "PASSWORD: "+pwd_example
print ""
print "HEX(SEED): "+str(hex(seed))
print "CIPHERTEXT: "+str(ciphertext)
#print "HEX(GUESSED_SEED): "+str(hex(decipher_seed))
print ""

print "orignal message is " + pwd_example
message = decode(decipher_seed, id_fxns)
print "decoded by the right seed, returned MESSAGE: "+message

message = decode(seed_guessedkey, id_fxns)
print "decoded by a guessed seed, returned MESSAGE: "+message
