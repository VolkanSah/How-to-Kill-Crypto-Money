import mnemonic

# Generate a seed phrase
seed = mnemonic.Mnemonic('english').generate(strength=128)
print("Seed Phrase:", seed)
