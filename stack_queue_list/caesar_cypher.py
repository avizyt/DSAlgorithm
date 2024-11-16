from collections import Counter
import string

# English letter frequency percentages (approximate)
ENGLISH_FREQ = {
    "E": 12.70,
    "T": 9.06,
    "A": 8.17,
    "O": 7.51,
    "I": 6.97,
    "N": 6.75,
    "S": 6.33,
    "H": 6.09,
    "R": 5.99,
    "D": 4.25,
    "L": 4.03,
    "C": 2.78,
    "U": 2.76,
    "M": 2.41,
    "W": 2.36,
    "F": 2.23,
    "G": 2.02,
    "Y": 1.97,
    "P": 1.93,
    "B": 1.49,
    "V": 0.98,
    "K": 0.77,
    "X": 0.15,
    "J": 0.10,
    "Q": 0.10,
    "Z": 0.07,
}


def caesarDecrypt(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            offset = ord("A") if char.isupper() else ord("a")
            decrypted.append(chr((ord(char) - offset + shift) % 26 + offset))
        else:
            decrypted.append(char)

    return "".join(decrypted)


def frequencyAnalysis(text):
    text = text.upper()
    total_letters = sum(1 for c in text if c.isalpha())
    freq = Counter(c for c in text if c.isalpha())
    return {char: (count / total_letters) * 100 for char, count in freq.items()}


def scoreDecryption(text):
    freqs = frequencyAnalysis(text)
    score = 0
    for char, freq in ENGLISH_FREQ.items():
        score += abs(freqs.get(char, 0) - freq)

    return score


def breakCaesarCipher(ciphertext):
    best_shift = None
    best_score = float("inf")
    best_decryption = None

    for shift in range(26):
        decrypted_text = caesarDecrypt(ciphertext, shift)
        score = scoreDecryption(decrypted_text)
        if score < best_score:
            best_score = score
            best_shift = shift
            best_decryption = decrypted_text

    return best_decryption, best_shift


def encryptCaesarCipher(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            offset = ord("A") if char.isupper() else ord("a")
            encrypted.append(chr((ord(char) + shift - offset) % 26 + offset))
        else:
            encrypted.append(char)

    return "".join(encrypted)


if __name__ == "__main__":
    ciphertext = "L ORYH SUREOHPV ZLWK FDXVDU FLSKHU"  # "I LOVE PROBLEMS WITH CAESAR CIPHER" encrypted with shift 3
    decrypted_text, shift = breakCaesarCipher(ciphertext)

    print(f"Decrypted Text: {decrypted_text}")
    print(f"Detected Shift: {shift}")
    print(f"Encrypted Text: {encryptCaesarCipher(decrypted_text, shift)}")
