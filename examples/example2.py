import mnemonic
import binascii

# Generate a seed phrase
seed = mnemonic.Mnemonic('english').generate(strength=128)

# Convert the seed phrase into a private key
private_key = binascii.hexlify(mnemonic.Mnemonic('english').to_seed(seed)).decode()
print("Private Key:", private_key)
