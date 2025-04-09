import base58

encoded = "iaPkqst7ig3Q7HQdnxYcYgUGyKsQXxFKckx6"
decoded = base58.b58decode(encoded)
print(decoded)
