import mnemonic
import binascii

# Read and validate a seed phrase
seed_phrase = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"

# Check if the seed phrase is valid
is_valid = mnemonic.Mnemonic('english').check(seed_phrase)
print("Is the seed phrase valid?", is_valid)

# Convert the valid seed phrase into a private key
if is_valid:
    private_key = binascii.hexlify(mnemonic.Mnemonic('english').to_seed(seed_phrase)).decode()
    print("Private Key:", private_key)
else:
    print("The seed phrase is invalid. Please provide a valid seed phrase.")
