def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key = key.upper()
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            pi = ord(ch) - base
            ki = ord(key[key_index % len(key)]) - ord('A')
            ci = (pi + ki) % 26
            ciphertext.append(chr(ci + base))
            key_index += 1
        else:
            ciphertext.append(ch)
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key = key.upper()
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            ci = ord(ch) - base
            ki = ord(key[key_index % len(key)]) - ord('A')
            pi = (ci - ki + 26) % 26
            plaintext.append(chr(pi + base))
            key_index += 1
        else:
            plaintext.append(ch)
    return "".join(plaintext)

def demo():
    examples = [
        ("Attack at dawn", "lemon"),
        ("Cryptography is an interesting field", "security")
    ]

    for pt, key in examples:
        ct = vigenere_encrypt(pt, key)
        dec = vigenere_decrypt(ct, key)
        print(f"평문: {pt}")
        print(f"키워드: {key}")
        print(f"암호화된 텍스트: {ct}")
        print(f"복호화된 텍스트: {dec}")
        print("-" * 60)

if __name__ == "__main__":
    demo()
