from collections import Counter
from itertools import permutations, cycle, permutations
from string import ascii_lowercase as key_symbols

cipher = bytes(map(int, open('59.txt', 'r').read().split(',')))

def decrypt(cipher: bytes) -> bytes:
  possible_keys = bytes(key_symbols, 'ascii')
  for encryption_key in permutations(possible_keys, 3):
    encoded = bytes([char ^ key for char, key in zip(cipher, cycle(encryption_key))])
    ascii_decoded = encoded.decode('ascii')

    has_common_characters = all([c in [mc for mc, _ in Counter(ascii_decoded).most_common()[:5]] for c in ' et'])
    has_common_words = all(word in ascii_decoded.lower() for word in [' the ', ' of '])
    if has_common_characters and has_common_words:
      return bytes([c for c in encoded if c >= 32])

print(decrypt(cipher))
print(sum(decrypt(cipher)))
