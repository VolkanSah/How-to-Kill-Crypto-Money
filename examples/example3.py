import mnemonic
import binascii
import hashlib
import hmac

# Generate a seed phrase
seed = mnemonic.Mnemonic('english').generate(strength=128)

# Convert the seed phrase into a private key
private_key = binascii.hexlify(mnemonic.Mnemonic('english').to_seed(seed)).decode()

# Example function to sign a transaction
def sign_transaction(transaction, private_key):
    # Convert the private key from hex to bytes
    private_key_bytes = binascii.unhexlify(private_key)
    
    # Create a HMAC object using the private key and SHA256
    h = hmac.new(private_key_bytes, transaction.encode('utf-8'), hashlib.sha256)
    
    # Generate the signature
    signature = h.hexdigest()
    
    return signature

# Hypothetical transaction data
transaction_data = "example_transaction_data"

# Sign the transaction
signed_transaction = sign_transaction(transaction_data, private_key)
print("Signed Transaction:", signed_transaction)
