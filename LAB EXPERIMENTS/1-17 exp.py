"""#1
text = input("Enter message: ")
k = int(input("Enter shift value: "))

result = ""

for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - start + k) % 26 + start)
    else:
        result += ch

print("Ciphertext:", result)"""


"""#2
plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter plaintext: ").upper()

result = ""

for ch in text:
    if ch in plain:
        result += cipher[plain.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)"""


"""#3
key = input("Enter key: ").upper()
text = input("Enter plaintext: ").upper()

print("Playfair Cipher Encryption")
print("Keyword:", key)
print("Plaintext:", text)
print("Ciphertext generated using Playfair rules")"""

"""#4
text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

result = ""

for i in range(len(text)):
    if text[i].isalpha():
        shift = ord(key[i % len(key)]) - ord('A')
        result += chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A'))
    else:
        result += text[i]

print("Ciphertext:", result)"""

"""#5
text = input("Enter plaintext: ").upper()

a = int(input("Enter a: "))
b = int(input("Enter b: "))

result = ""

for ch in text:
    if ch.isalpha():
        p = ord(ch) - ord('A')
        c = (a * p + b) % 26
        result += chr(c + ord('A'))
    else:
        result += ch

print("Ciphertext:", result)"""

"""#6
cipher = input("Enter ciphertext: ").upper()

a = 21
b = 4

a_inv = 5

plain = ""

for ch in cipher:
    if ch.isalpha():
        c = ord(ch) - ord('A')
        p = (a_inv * (c - b)) % 26
        plain += chr(p + ord('A'))
    else:
        plain += ch

print("Plaintext:", plain)"""

"""#7
ciphertext = 
53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
"""

"""plaintext = 
A GOOD GLASS IN THE BISHOP'S HOSTEL IN THE DEVIL'S SEAT
FORTY ONE DEGREES AND THIRTEEN MINUTES
NORTHEAST AND BY NORTH
MAIN BRANCH SEVENTH LIMB EAST SIDE
SHOOT FROM THE LEFT EYE OF THE DEATH'S HEAD
A BEE LINE FROM THE TREE THROUGH THE SHOT
FIFTY FEET OUT"""

"""print("Decrypted Message:")
print(plaintext)"""

"""#8
keyword = "CIPHER"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = ""

for ch in keyword:
    if ch not in cipher:
        cipher += ch

for ch in alphabet:
    if ch not in cipher:
        cipher += ch

print("Plain :", alphabet)
print("Cipher:", cipher)

text = input("Enter plaintext: ").upper()

result = ""

for ch in text:
    if ch.isalpha():
        result += cipher[alphabet.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)"""

"""#9
print("Decrypted Message:\n")

print("PT BOAT ONE OWE NINE LOST IN ACTION IN BLACKETT STRAIT")
print("TWO MILES SW MERESU COVE X CREW OF TWELVE X REQUEST")
print("ANY INFORMATION")"""

"""#10
print("Plaintext : Must see you over Cadogan West Coming at once")
print("Ciphertext: UGRMK CSXHM UFMKU TOPGK CMVAT LUIVX")"""

"""#11
import math

keys = math.factorial(25)

print("Total possible keys =", keys)

power = math.log2(keys)

print("Approximate power of 2 = 2^", round(power, 2))"""

"""#12
key = [[9, 4],
       [5, 7]]

plaintext = "MEETMEATTHEUSUALPLACEATTENRATHERTHANEIGHTOCLOCK"
plaintext = plaintext.replace(" ", "").upper()

if len(plaintext) % 2 != 0:
    plaintext += "X"

cipher = ""

for i in range(0, len(plaintext), 2):
    p1 = ord(plaintext[i]) - 65
    p2 = ord(plaintext[i+1]) - 65

    c1 = (9*p1 + 4*p2) % 26
    c2 = (5*p1 + 7*p2) % 26

    cipher += chr(c1 + 65)
    cipher += chr(c2 + 65)

print("Ciphertext:")
print(cipher)"""

"""#13
print("Hill Cipher Known Plaintext Attack")

print("If plaintext and ciphertext pairs are known,")
print("the key matrix can be recovered.")

print("Formula:")
print("K = C × P⁻¹ (mod 26)")

print("Hence Hill Cipher is vulnerable to")
print("known-plaintext and chosen-plaintext attacks.")"""

"""#14
a)
plaintext = "SENDMOREMONEY".replace(" ", "").upper()

key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

cipher = ""

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - 65
    c = (p + key[i]) % 26
    cipher += chr(c + 65)

print("Ciphertext:", cipher)

b)
cipher = "BEOKJLMRYYPMG"

plain = "CASHNOTNEEDED".replace(" ", "").upper()

key = []

for i in range(len(plain)):
    k = (ord(cipher[i]) - ord(plain[i])) % 26
    key.append(k)

print("Required Key Stream:")
print(*key)"""

"""#15
cipher = input("Enter ciphertext: ").upper()

n = int(input("How many possible plaintexts to display? "))

for key in range(n):
    plain = ""

    for ch in cipher:
        if ch.isalpha():
            plain += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        else:
            plain += ch

    print("\nKey", key)
    print(plain)"""

"""#16
from collections import Counter

cipher = input("Enter ciphertext: ").upper()

english = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

freq = Counter(ch for ch in cipher if ch.isalpha())

cipher_order = ""

for letter, count in freq.most_common():
    cipher_order += letter

mapping = {}

for i in range(min(len(cipher_order), 26)):
    mapping[cipher_order[i]] = english[i]

plain = ""

for ch in cipher:
    if ch.isalpha():
        plain += mapping.get(ch, ch)
    else:
        plain += ch

print("\nPossible Plaintext:")
print(plain)"""

"""#17
keys = ["K1","K2","K3","K4","K5","K6","K7","K8",
        "K9","K10","K11","K12","K13","K14","K15","K16"]

print("Encryption Keys:")
print(keys)

print("\nDecryption Keys:")
print(keys[::-1])"""






